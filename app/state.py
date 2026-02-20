"""Project state persistence — save/load project state as JSON files."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import PROJECTS_DIR
from app.display import show_error


def _project_path(name: str) -> Path:
    """Return the JSON file path for a project by name."""
    return PROJECTS_DIR / f"{name}.json"


def save_project(project: dict[str, Any]) -> None:
    """Save project state to projects/{name}.json."""
    project["updated_at"] = datetime.now(timezone.utc).isoformat()
    path = _project_path(project["name"])
    path.write_text(json.dumps(project, indent=2, ensure_ascii=False), encoding="utf-8")


def load_project(name: str) -> dict[str, Any] | None:
    """Load a project from JSON. Returns None if not found or corrupted."""
    path = _project_path(name)
    if not path.exists():
        show_error(f"Project '{name}' not found.")
        return None

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        show_error(f"Project file corrupted: {exc}")
        return None


def list_projects() -> list[dict[str, Any]]:
    """List all saved projects with summary info.

    Returns a list of dicts with keys: name, current_step, total_steps, workflow_name.
    """
    projects: list[dict[str, Any]] = []
    for path in sorted(PROJECTS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            projects.append({
                "name": data["name"],
                "current_step": data.get("current_step", 0),
                "total_steps": len(data.get("workflow", [])),
                "workflow_name": data.get("answers", {}).get("complexity", "unknown").title(),
            })
        except (json.JSONDecodeError, KeyError, OSError):
            # Skip corrupted files
            continue
    return projects


def delete_project(name: str) -> bool:
    """Remove a project JSON file. Returns True if deleted."""
    path = _project_path(name)
    if path.exists():
        path.unlink()
        return True
    return False
