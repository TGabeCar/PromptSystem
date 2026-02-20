"""One-shot prompts — single-use workflows with no project state."""

from __future__ import annotations

import re
from typing import Any

import yaml

from app.clipboard_util import copy_prompt_to_clipboard_or_file
from app.config import PROMPTS_DIR, WORKFLOWS_DIR
from app.display import (
    console,
    get_input,
    get_multiline_input,
    show_error,
    show_info,
    show_menu,
    show_step,
    show_success,
)


def _load_oneshot_config() -> tuple[dict[str, str], list[dict[str, Any]]]:
    """Load oneshot config. Returns (categories_id_to_label, prompts list)."""
    path = WORKFLOWS_DIR / "oneshot.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    categories = data.get("categories") or {}
    prompts = data.get("prompts", [])
    return categories, prompts


def _group_prompts_by_category(
    prompts: list[dict[str, Any]], categories: dict[str, str]
) -> tuple[list[str], dict[str, list[dict[str, Any]]]]:
    """Group prompts by category. Returns (ordered category ids, category_id -> prompts)."""
    by_category: dict[str, list[dict[str, Any]]] = {}
    for p in prompts:
        cat = p.get("category", "other")
        by_category.setdefault(cat, []).append(p)

    category_order = list(categories.keys())
    ordered_ids = [c for c in category_order if c in by_category]
    for c in sorted(by_category):
        if c not in ordered_ids:
            ordered_ids.append(c)
    return ordered_ids, by_category


def _choose_category(
    ordered_ids: list[str],
    by_category: dict[str, list[dict[str, Any]]],
    categories: dict[str, str],
) -> str | None:
    """
    Show 'What do you need?' menu. Returns chosen category id, 'all', or None for back.
    """
    if not ordered_ids:
        options = ["All prompts", "Back to Main Menu"]
        choice = show_menu("Other Prompts — What do you need?", options)
        if choice == 0 or choice == 2:
            return None
        return "all"

    labels = [categories.get(cid, cid.replace("_", " ").title()) for cid in ordered_ids]
    options = labels + ["Show all prompts", "Back to Main Menu"]
    choice = show_menu("Other Prompts — What do you need?", options)

    if choice == 0 or choice == len(options):
        return None
    if choice == len(options) - 1:
        return "all"
    return ordered_ids[choice - 1]


def _choose_prompt(
    prompts_in_category: list[dict[str, Any]], category_label: str
) -> dict[str, Any] | None:
    """Show prompt list for a category. Returns selected prompt dict or None for Back."""
    options = [p["name"] for p in prompts_in_category] + ["Back"]
    choice = show_menu(category_label, options)
    if choice == 0 or choice == len(options):
        return None
    return prompts_in_category[choice - 1]


def _load_prompt_body(filename: str) -> str | None:
    """Load a prompt file and return the body (everything after the second '---')."""
    path = PROMPTS_DIR / filename
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].strip()
    return content.strip()


def _inject_variables(template: str, values: dict[str, str]) -> str:
    """Replace {{VARIABLE}} placeholders with values. Missing/empty → placeholder."""
    def replacer(match: re.Match[str]) -> str:
        var_name = match.group(1)
        val = values.get(var_name, "").strip()
        return val if val else "[Not specified]"

    return re.sub(r"\{\{(\w+)\}\}", replacer, template)


MULTILINE_KEYS = frozenset((
    "NEED", "TOPIC", "SITUATION", "CAPABILITY", "SUBJECT", "PROCESS",
    "OPTIONS", "VENDORS", "APP_IDEA", "BUG_DESC", "SCOPE", "DOC_TOPIC", "EXISTING_DOC",
    "FEATURE_DESC",
))

CANCEL_INPUTS = frozenset(("q", "cancel", "/cancel"))
BACK_INPUTS = frozenset(("b", "back"))


def _is_cancel(raw: str) -> bool:
    """True if user wants to abort to prompt list."""
    return raw.strip().lower() in CANCEL_INPUTS


def _is_back(raw: str) -> bool:
    """True if user wants to go to previous question."""
    return raw.strip().lower() in BACK_INPUTS


def _collect_inputs(selected: dict[str, Any]) -> dict[str, str] | None:
    """Collect input values for a oneshot prompt. Returns None if user cancels."""
    inputs_spec = selected.get("inputs", [])
    if not inputs_spec:
        return {}
    values: dict[str, str] = {}
    i = 0
    while i < len(inputs_spec):
        inp = inputs_spec[i]
        key = inp["key"]
        prompt_text = inp["prompt"]
        nav_hint = "B = previous · q = cancel" if i > 0 else "q = cancel"
        single_line_commands = CANCEL_INPUTS | BACK_INPUTS

        if key in MULTILINE_KEYS:
            raw = get_multiline_input(
                prompt_text,
                nav_hint=nav_hint,
                single_line_commands=single_line_commands,
            )
        else:
            raw = get_input(prompt_text, nav_hint=nav_hint)

        if _is_cancel(raw):
            return None
        if _is_back(raw):
            if i > 0:
                i -= 1
                show_info("Previous question.")
                continue
            show_info("No previous question.")
            continue

        values[key] = raw
        i += 1
    return values


def _run_sequence(selected: dict[str, Any], initial_values: dict[str, str]) -> None:
    """Run a multi-step sequence: assemble prompts, copy to clipboard, optionally capture responses.

    Each step's prompt is assembled with all accumulated values (initial inputs +
    responses from previous steps). Steps with ``stores_as`` capture the AI's response
    for injection into later steps. Steps without it just wait for the user to continue.
    """
    steps: list[dict[str, Any]] = selected["steps"]
    total = len(steps)
    values = dict(initial_values)

    for step_idx, step in enumerate(steps):
        step_num = step_idx + 1
        is_last = step_num == total

        body = _load_prompt_body(step["prompt_file"])
        if body is None:
            show_error(f"Prompt file not found: {step['prompt_file']} — skipping step.")
            continue

        assembled = _inject_variables(body, values)
        target_tool = step.get("target_tool", "Any AI")

        show_step(step_num, total, step["name"], target_tool)

        clipboard_ok, fallback_path = copy_prompt_to_clipboard_or_file(assembled)
        if clipboard_ok:
            show_success("Prompt copied to clipboard")
            show_info(f"Paste into: {target_tool}")
        else:
            show_error(
                "Clipboard copy failed (long prompts often fail when Windows Clipboard History is enabled)."
            )
            if fallback_path:
                show_info(f"Prompt saved to: {fallback_path}")
            show_error("Displaying prompt:")
            console.print()
            console.print(assembled)
            console.print()

        # Show step-specific note if configured
        note = step.get("note", "")
        if note:
            console.print()
            console.print(f"  [yellow]Note:[/yellow] {note}")

        if is_last:
            break

        stores_as = step.get("stores_as", "")

        if stores_as:
            # Intermediate step that captures a response for injection into later steps
            console.print()
            console.print(
                "  After pasting into the AI tool and getting a response,\n"
                "  paste the response here (press Enter twice when done).\n"
            )
            console.print(f"  Or: [V]iew prompt  [Q]uit")
            console.print()

            while True:
                response_text = get_multiline_input(
                    "",
                    single_line_commands=CANCEL_INPUTS | {"v"},
                )
                stripped = response_text.strip().lower()

                if stripped == "q":
                    show_info("Sequence cancelled.")
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
                    continue

                if response_text.strip():
                    values[stores_as] = response_text
                    show_success("Response captured. Moving to next step...")
                    break

                show_info("Empty response. Please paste the AI's response, or press Q to quit.")
        else:
            # Intermediate step with no response capture — wait for user to continue
            console.print()
            console.print(f"  [V]iew prompt  [Q]uit  or press [Enter] to continue to next step")
            console.print()

            while True:
                raw = get_input("")
                stripped = raw.strip().lower()

                if stripped == "q":
                    show_info("Sequence cancelled.")
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
                    continue

                break


def _run_single_oneshot(
    categories: dict[str, str],
    ordered_ids: list[str],
    by_category: dict[str, list[dict[str, Any]]],
    all_prompts: list[dict[str, Any]],
) -> bool:
    """Run one one-shot flow: choose category → choose prompt → inputs → copy. Returns True to run another."""
    cat = _choose_category(ordered_ids, by_category, categories)
    if cat is None:
        return False

    if cat == "all":
        prompts_to_show = all_prompts
        category_label = "All prompts — choose one"
    else:
        prompts_to_show = by_category[cat]
        category_label = categories.get(cat, cat.replace("_", " ").title())

    while True:
        selected = _choose_prompt(prompts_to_show, category_label)
        if selected is None:
            return _run_single_oneshot(categories, ordered_ids, by_category, all_prompts)

        values = _collect_inputs(selected)
        if values is None:
            show_info("Cancelled. Returning to prompt list.")
            continue
        break

    # Multi-step sequence (e.g. feature transfer: export → import)
    if selected.get("type") == "sequence" and "steps" in selected:
        _run_sequence(selected, values)
        next_choice = show_menu("What next?", [
            "Run another one-shot prompt",
            "Back to Main Menu",
        ])
        return next_choice == 1

    body = _load_prompt_body(selected["prompt_file"])
    if body is None:
        show_error(f"Prompt file not found: {selected['prompt_file']}")
        return True

    assembled = _inject_variables(body, values)

    target_tool = selected.get("target_tool", "Any AI")
    show_step(1, 1, selected["name"], target_tool)

    clipboard_ok, fallback_path = copy_prompt_to_clipboard_or_file(assembled)
    if clipboard_ok:
        show_success("Prompt copied to clipboard")
        show_info(f"Paste into: {target_tool}")
    else:
        show_error(
            "Clipboard copy failed (long prompts often fail when Windows Clipboard History is enabled)."
        )
        if fallback_path:
            show_info(f"Prompt saved to: {fallback_path}")
        show_error("Displaying prompt:")
        console.print(assembled)

    next_choice = show_menu("What next?", [
        "Run another one-shot prompt",
        "Back to Main Menu",
    ])
    return next_choice == 1


def run_oneshot() -> None:
    """Category-based one-shot flow: choose category → prompt → inputs → copy; run another or back."""
    categories, prompts = _load_oneshot_config()
    if not prompts:
        show_error("No one-shot prompts configured. Check workflows/oneshot.yaml")
        return

    ordered_ids, by_category = _group_prompts_by_category(prompts, categories)

    while _run_single_oneshot(categories, ordered_ids, by_category, prompts):
        pass
