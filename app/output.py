"""Generate final output files (docs, cursor rules, cursor commands) into a target project directory."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from app.config import CURSOR_TEMPLATES_DIR
from app.display import get_input, show_error, show_info, show_success


# Tech stack → cursor rule files to copy
_TECH_RULES: dict[str, list[str]] = {
    "python": ["python.mdc"],
    "dotnet": ["dotnet.mdc"],
    "web": ["web-frontend.mdc"],
    "mixed": ["python.mdc", "dotnet.mdc", "web-frontend.mdc"],
}


def _write_file(path: Path, content: str) -> None:
    """Write content to a file, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _copy_file(src: Path, dest: Path) -> None:
    """Copy a file, creating parent directories as needed."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def _generate_project_context(project: dict[str, Any]) -> str:
    """Generate the 001-project-context.mdc content from the template.

    Uses structured questionnaire answers (reliable) for core fields and references
    docs/ files for detailed information rather than attempting fragile regex extraction
    from free-form AI responses.
    """
    template_path = CURSOR_TEMPLATES_DIR / "rules" / "001-project-context.mdc.template"
    if not template_path.exists():
        return ""

    template = template_path.read_text(encoding="utf-8")
    answers = project.get("answers", {})
    responses = project.get("responses", {})

    # Structured data from questionnaire (reliable)
    project_name = project.get("name", "unknown")
    project_desc = responses.get("PROJECT_DESCRIPTION", answers.get("project_description", ""))
    project_type = answers.get("project_type", "unknown")
    complexity = answers.get("complexity", "unknown")

    # Language-agnostic: research step recommends stack; all tech rules are copied
    has_research = bool(responses.get("RESEARCH_DOC"))
    tech_details = "Language-agnostic — choose best tool for the task."
    if has_research:
        tech_details += "\nSee @docs/RESEARCH.md for recommended language, versions, dependencies, and API references."

    # Doc URLs — point to RESEARCH.md rather than trying to extract URLs
    if has_research:
        doc_urls = (
            "See @docs/RESEARCH.md for the complete documentation index.\n"
            "Add all URLs from the Documentation Index table to Cursor Settings > Features > Docs."
        )
    else:
        doc_urls = "No research document available — verify documentation URLs manually"

    # Architecture — point to architecture doc rather than extracting
    has_arch = bool(responses.get("ARCHITECTURE") or responses.get("PRD_ARCHITECTURE"))
    if has_arch:
        arch_pattern = "See @docs/ARCHITECTURE.md for complete architecture design, patterns, and component interfaces"
    else:
        arch_pattern = "No architecture document available"

    # Build-vs-buy — point to landscape doc
    has_landscape = bool(responses.get("LANDSCAPE_ANALYSIS"))
    if has_landscape:
        dont_build = "See @docs/LANDSCAPE.md for build-vs-buy decisions and existing solutions to leverage"
    else:
        dont_build = "No landscape analysis performed"

    # Manual setup (outside Cursor) — only when External Setup Guide was generated
    if responses.get("EXTERNAL_SETUP"):
        external_setup_section = (
            "## Manual Setup (Outside Cursor)\n\n"
            "See @docs/EXTERNAL_SETUP.md for accounts, API keys, cloud, and database setup to complete outside the IDE."
        )
    else:
        external_setup_section = ""

    # Replace template variables
    replacements = {
        "PROJECT_NAME": project_name,
        "PROJECT_DESCRIPTION": project_desc[:500] if project_desc else "No description",
        "TECH_STACK": tech_details,
        "DOC_URLS": doc_urls,
        "ARCHITECTURE_PATTERN": arch_pattern,
        "DONT_BUILD": dont_build,
        "PROJECT_TYPE": project_type.replace("_", " ").title(),
        "COMPLEXITY": complexity.title(),
        "EXTERNAL_SETUP_SECTION": external_setup_section,
    }

    result = template
    for key, value in replacements.items():
        result = result.replace("{{" + key + "}}", value)

    return result


def generate_output(project: dict[str, Any]) -> None:
    """Generate all output files in the user's target project directory."""
    if project.get("project_path"):
        target = Path(project["project_path"]).resolve()
    else:
        target_str = get_input("Enter the path to your project directory:")
        if not target_str:
            show_error("No path provided. Skipping output generation.")
            return
        target = Path(target_str).expanduser().resolve()

    if not target.exists():
        show_info(f"Directory does not exist. Creating: {target}")
        target.mkdir(parents=True, exist_ok=True)

    answers = project.get("answers", {})
    responses = project.get("responses", {})
    created_files: list[str] = []

    # --- docs/ folder ---
    docs_dir = target / "docs"

    # Map stored responses to output documents based on workflow steps
    for step in project.get("workflow", []):
        output_doc = step.get("output_doc")
        stores_as = step.get("stores_as", "")
        if output_doc and stores_as in responses:
            doc_path = docs_dir / output_doc
            _write_file(doc_path, responses[stores_as])
            created_files.append(f"docs/{output_doc}")

    # For standard tier combined PRD+Architecture, also write ARCHITECTURE.md
    if "PRD_ARCHITECTURE" in responses:
        arch_path = docs_dir / "ARCHITECTURE.md"
        if not arch_path.exists():
            _write_file(arch_path, responses["PRD_ARCHITECTURE"])
            created_files.append("docs/ARCHITECTURE.md")

    # --- .cursor/rules/ folder ---
    rules_src = CURSOR_TEMPLATES_DIR / "rules"
    rules_dest = target / ".cursor" / "rules"

    # Always copy 000-core.mdc
    core_src = rules_src / "000-core.mdc"
    if core_src.exists():
        _copy_file(core_src, rules_dest / "000-core.mdc")
        created_files.append(".cursor/rules/000-core.mdc")

    # Copy all tech rules (language-agnostic; research recommends stack)
    for rule_file in _TECH_RULES.get("mixed", []):
        src = rules_src / rule_file
        if src.exists():
            _copy_file(src, rules_dest / rule_file)
            created_files.append(f".cursor/rules/{rule_file}")

    # Security rules for customer-facing products
    if answers.get("project_type") == "customer_facing":
        sec_src = rules_src / "security.mdc"
        if sec_src.exists():
            _copy_file(sec_src, rules_dest / "security.mdc")
            created_files.append(".cursor/rules/security.mdc")

    # Generate project-context rule from template
    context_content = _generate_project_context(project)
    if context_content:
        _write_file(rules_dest / "001-project-context.mdc", context_content)
        created_files.append(".cursor/rules/001-project-context.mdc")

    # --- .cursor/commands/ folder ---
    commands_src = CURSOR_TEMPLATES_DIR / "commands"
    commands_dest = target / ".cursor" / "commands"

    if commands_src.exists():
        for cmd_file in sorted(commands_src.glob("*.md")):
            _copy_file(cmd_file, commands_dest / cmd_file.name)
            created_files.append(f".cursor/commands/{cmd_file.name}")

    # --- Summary ---
    from app.display import console

    console.print()
    console.print("[bold green]Generating output files...[/bold green]")
    for f in created_files:
        show_success(f)

    console.print()
    show_success(f"Done! Open your project in Cursor and start building.")
    show_info(f"Project directory: {target}")
