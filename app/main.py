"""Main menu loop for the AI Workflow Manager CLI."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.config import PROMPTS_DIR, WORKFLOWS_DIR
from app.display import (
    console,
    get_input,
    show_error,
    show_header,
    show_info,
    show_menu,
    show_success,
)
from app.oneshot import run_oneshot
from app.path_picker import get_project_directory
from app.questionnaire import run_questionnaire
from app.runner import run_workflow
from app.sequencer import get_workflow
from app.state import delete_project, list_projects, load_project, save_project


def _project_submenu() -> None:
    """Submenu for project-related actions."""
    while True:
        choice = show_menu("Create Project", [
            "New Project",
            "Continue Project",
            "List Projects",
            "Delete Project",
            "Back to Main Menu",
        ])
        if choice == 0:
            return
        if choice == 1:
            _new_project()
            return
        if choice == 2:
            _continue_project()
            return
        if choice == 3:
            _list_projects()
            return
        if choice == 4:
            _delete_project()
            return
        if choice == 5:
            return


def _new_project() -> None:
    """Create a new project from questionnaire answers and start the workflow."""
    answers = run_questionnaire()
    if answers is None:
        show_info("Cancelled.")
        return

    # Build the workflow step sequence
    try:
        workflow = get_workflow(answers)
    except Exception as exc:
        show_error(f"Failed to load workflow: {exc}")
        return

    # Create project state
    project: dict[str, Any] = {
        "name": answers["name"],
        "answers": answers,
        "workflow": workflow,
        "current_step": 0,
        "responses": {
            "PROJECT_DESCRIPTION": answers.get("project_description", ""),
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }

    project_dir = get_project_directory()
    if project_dir is not None:
        project["project_path"] = str(project_dir)
        show_success(f"Project folder: {project_dir}")

    save_project(project)

    total = len(workflow)
    workflow_name = answers["complexity"].title()
    show_success(f"Project created: {answers['name']}")
    show_success(f"Workflow: {workflow_name} ({total} steps)")
    show_info("Starting Step 1...")

    run_workflow(project)


def _continue_project() -> None:
    """Resume a saved project."""
    projects = list_projects()
    if not projects:
        show_info("No saved projects found.")
        return

    options = [
        f"{p['name']} (Step {p['current_step'] + 1} of {p['total_steps']} — {p['workflow_name']})"
        for p in projects
    ]
    choice = show_menu("Select a project to continue", options)
    if choice == 0:
        return
    selected = projects[choice - 1]

    project = load_project(selected["name"])
    if project is None:
        return

    step = project.get("current_step", 0) + 1
    total = len(project.get("workflow", []))
    show_info(f"Resuming {selected['name']} at Step {step} of {total}...")

    run_workflow(project)


def _list_projects() -> None:
    """Display all saved projects with their status."""
    projects = list_projects()
    if not projects:
        show_info("No saved projects found.")
        return

    console.print()
    console.print("[bold]Saved Projects:[/bold]")
    console.print()
    for p in projects:
        step = p["current_step"] + 1
        total = p["total_steps"]
        status = "Complete" if p["current_step"] >= total else f"Step {step} of {total}"
        console.print(f"  [cyan]{p['name']}[/cyan] — {status} ({p['workflow_name']})")
    console.print()


def _delete_project() -> None:
    """Delete a saved project after confirmation."""
    projects = list_projects()
    if not projects:
        show_info("No saved projects found.")
        return

    options = [
        f"{p['name']} (Step {p['current_step'] + 1} of {p['total_steps']})"
        for p in projects
    ] + ["Cancel"]
    choice = show_menu("Select a project to delete", options)
    if choice == 0 or choice == len(options):
        show_info("Cancelled.")
        return

    selected = projects[choice - 1]
    name = selected["name"]
    confirm = get_input(f"Delete project '{name}'? This cannot be undone. (y/n):").strip().lower()
    if confirm != "y":
        show_info("Cancelled.")
        return

    if delete_project(name):
        show_success(f"Project '{name}' deleted.")
    else:
        show_error(f"Could not delete '{name}'.")


def _settings() -> None:
    """Show editable directory paths."""
    console.print()
    console.print("[bold]Settings & Paths[/bold]")
    console.print()
    console.print(f"  Prompts directory:  [cyan]{PROMPTS_DIR}[/cyan]")
    console.print(f"  Workflows directory: [cyan]{WORKFLOWS_DIR}[/cyan]")
    console.print()
    show_info("Edit prompt .md files or workflow .yaml files in these directories to customize.")
    console.print()


def main() -> None:
    """Application entry point — main menu loop."""
    show_header("AI Workflow Manager")

    while True:
        choice = show_menu("Main Menu", [
            "Create Project",
            "Other Prompts",
            "Settings",
            "Exit",
        ], allow_quit=False)

        if choice == 4:
            show_info("Goodbye.")
            break
        if choice == 1:
            _project_submenu()
        elif choice == 2:
            run_oneshot()
        elif choice == 3:
            _settings()
