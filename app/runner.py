"""Core workflow execution loop — load prompts, inject context, clipboard, capture responses."""

from __future__ import annotations

import re
import secrets
from pathlib import Path
from typing import Any

from app.clipboard_util import copy_prompt_to_clipboard_or_file
from app.config import PROMPTS_DIR
from app.display import (
    console,
    get_multiline_input,
    show_error,
    show_info,
    show_step,
    show_success,
)
from app.output import _write_file
from app.state import save_project


def _load_prompt_body(filename: str) -> str | None:
    """Load a prompt file and return the body (everything after the second '---').

    Returns None if the file doesn't exist.
    """
    path = PROMPTS_DIR / filename
    if not path.exists():
        return None

    content = path.read_text(encoding="utf-8")

    # Split on the second --- to separate frontmatter from body
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].strip()

    # No frontmatter — treat entire content as the body
    return content.strip()


def _get_doc_variable_map(workflow: list[dict[str, Any]]) -> dict[str, str]:
    """Build mapping from stores_as variable name to output_doc filename for steps that write to docs/."""
    result: dict[str, str] = {}
    for s in workflow:
        output_doc = s.get("output_doc")
        stores_as = s.get("stores_as", "")
        if output_doc and stores_as:
            result[stores_as] = output_doc
    return result


def _inject_variables(template: str, responses: dict[str, str]) -> str:
    """Replace all {{VARIABLE_NAME}} placeholders with stored response values.

    Missing variables are replaced with a placeholder message.
    """
    def replacer(match: re.Match[str]) -> str:
        var_name = match.group(1)
        return responses.get(var_name, "[Not provided — this step was skipped]")

    return re.sub(r"\{\{(\w+)\}\}", replacer, template)


def _is_cursor_only_target(target_tool: str) -> bool:
    """True if this step's prompt is intended for Cursor only (so @docs/ refs work)."""
    t = (target_tool or "").strip().lower()
    return t == "cursor"


def _responses_for_prompt(
    project: dict[str, Any],
    doc_var_to_output_doc: dict[str, str],
    step: dict[str, Any],
) -> dict[str, str]:
    """Use short @docs/ references only when the step target is Cursor. For Poppy/Grok/other, inject full doc content so the prompt is self-contained when pasted."""
    responses = project["responses"]
    use_short_refs = (
        project.get("project_path")
        and doc_var_to_output_doc
        and _is_cursor_only_target(step.get("target_tool", ""))
    )
    if not use_short_refs:
        return responses
    effective = dict(responses)
    for var_name, output_doc in doc_var_to_output_doc.items():
        if var_name in effective:
            effective[var_name] = (
                f"[Document already in project — reference with @docs/{output_doc} in Cursor.]"
            )
    return effective


def run_workflow(project: dict[str, Any]) -> None:
    """Execute the workflow from the current step onward.

    For each step:
    1. Load and assemble the prompt with injected variables
    2. Copy to clipboard
    3. Show step header and navigation options
    4. Capture user's pasted AI response
    5. Store response and advance
    6. Save state after each step
    """
    workflow: list[dict[str, Any]] = project["workflow"]
    total_steps = len(workflow)
    doc_var_to_output_doc = _get_doc_variable_map(workflow)

    while project["current_step"] < total_steps:
        step_idx = project["current_step"]
        step = workflow[step_idx]
        step_num = step_idx + 1

        # Load prompt template
        prompt_file = step.get("prompt_file", "")
        body = _load_prompt_body(prompt_file)
        if body is None:
            show_error(f"Prompt file not found: {prompt_file} — skipping step.")
            project["current_step"] += 1
            save_project(project)
            continue

        # Inject stored responses: full doc content for Poppy/Grok (self-contained); short @docs/ refs only when target is Cursor
        effective_responses = _responses_for_prompt(project, doc_var_to_output_doc, step)
        assembled = _inject_variables(body, effective_responses)

        # Copy to clipboard (or save to file if clipboard fails, e.g. long prompt + Windows Clipboard History)
        clipboard_ok, fallback_path = copy_prompt_to_clipboard_or_file(assembled)

        # Display step header
        show_step(step_num, total_steps, step["name"], step.get("target_tool", ""))

        if clipboard_ok:
            show_success("Prompt copied to clipboard")
        else:
            if fallback_path:
                show_info("Clipboard was busy (common with Windows Clipboard History). Prompt saved to:")
                show_info(f"  {fallback_path}")
                show_info("Open that file to copy, or use [V]iew to see the full prompt.")
            else:
                show_error("Clipboard copy failed. Use [V]iew to see the full prompt and copy manually.")
            lines = assembled.splitlines()
            if len(lines) > 30:
                console.print()
                console.print("\n".join(lines[:20]))
                console.print(f"\n  [dim]... [{len(lines) - 25} more lines — press V to view full prompt] ...[/dim]\n")
                console.print("\n".join(lines[-5:]))
                console.print()
            else:
                console.print()
                console.print(assembled)
                console.print()

        # Show which context was injected
        injects = step.get("injects", [])
        injected = [v for v in injects if v in project["responses"]]
        if injected:
            show_info(f"Context injected: {', '.join(injected)}")

        # Show navigation options and end-marker so pasted content with blank lines doesn't split across steps
        end_marker = f"PASTE_END_{secrets.token_hex(4)}"
        console.print()
        console.print(
            "  After pasting into the AI tool and getting a response, paste the response below."
        )
        skippable_hint = "[S]kip  " if step.get("skippable", False) else ""
        back_hint = "[B]ack  " if step_idx > 0 else ""
        console.print(f"  Or: {skippable_hint}{back_hint}[V]iew prompt  [Q]uit (progress saved)")
        console.print(f"  [dim]When finished, type the marker below or press Enter 3 times.[/dim]")
        console.print()

        # Build single-line commands so Q/V/etc return immediately (no Enter twice)
        nav_commands = {"q", "v"}
        if step_idx > 0:
            nav_commands.add("b")
        if step.get("skippable", False):
            nav_commands.add("s")

        # Capture response or navigation command
        response_text = get_multiline_input(
            "", single_line_commands=nav_commands, end_marker=end_marker
        )

        # Check for single-character navigation commands
        stripped = response_text.strip().lower()

        if stripped == "q":
            save_project(project)
            show_success("Progress saved. Returning to main menu.")
            return

        if stripped == "v":
            console.print()
            console.rule("[dim]Full prompt[/dim]")
            console.print(assembled)
            console.rule()
            ok, path = copy_prompt_to_clipboard_or_file(assembled)
            if ok:
                show_info("Prompt re-copied to clipboard.")
            elif path:
                show_info(f"Clipboard still unavailable. Prompt saved to: {path}")
            else:
                show_info("Clipboard unavailable — copy from above.")
            # Don't advance — re-run this step's input capture
            continue

        if stripped == "b" and step_idx > 0:
            project["current_step"] -= 1
            save_project(project)
            show_info("Going back one step.")
            continue

        if stripped == "s" and step.get("skippable", False):
            project["current_step"] += 1
            save_project(project)
            show_info(f"Skipped: {step['name']}")
            continue

        # If we got actual content, store it
        if response_text.strip():
            stores_as = step.get("stores_as", "")
            if stores_as:
                project["responses"][stores_as] = response_text
                show_success(f"Response saved as {stores_as}")

                # Brainstorm step: also update PROJECT_DESCRIPTION
                if step.get("id") == "brainstorm":
                    project["responses"]["PROJECT_DESCRIPTION"] = response_text
                    show_info("PROJECT_DESCRIPTION updated with brainstormed version.")

                # Write to project docs/ when project_path is set and this step has output_doc
                output_doc = step.get("output_doc")
                project_path = project.get("project_path")
                if output_doc and project_path:
                    docs_dir = Path(project_path) / "docs"
                    doc_path = docs_dir / output_doc
                    _write_file(doc_path, response_text)
                    show_info(f"Written to docs/{output_doc}")
        else:
            show_info("Empty response — step recorded but no content stored.")

        # Advance to next step
        project["current_step"] += 1
        save_project(project)

    # All steps complete — trigger output generation
    from app.output import generate_output

    console.print()
    console.rule("[bold green]All steps complete![/bold green]")
    console.print()
    generate_output(project)
