"""Maps questionnaire answers to an ordered workflow step list."""

from __future__ import annotations

import copy
from typing import Any

import yaml

from app.config import WORKFLOWS_DIR


def _load_yaml(filename: str) -> dict[str, Any]:
    """Load and parse a workflow YAML file."""
    path = WORKFLOWS_DIR / filename
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _remap_injects(steps: list[dict[str, Any]], mapping: dict[str, str]) -> list[dict[str, Any]]:
    """Replace variable names in each step's 'injects' list according to mapping.

    For example, when a standard-tier collaborative project uses PRD_ARCHITECTURE
    instead of ARCHITECTURE, this replaces references so the correct stored
    response is injected.
    """
    remapped: list[dict[str, Any]] = []
    for step in steps:
        step = copy.deepcopy(step)
        if step.get("injects"):
            step["injects"] = [mapping.get(v, v) for v in step["injects"]]
        remapped.append(step)
    return remapped


def get_workflow(answers: dict[str, Any]) -> list[dict[str, Any]]:
    """Build the ordered workflow step list from questionnaire answers.

    Loads the base workflow YAML for the selected complexity tier, then:
    - Prepends the brainstorm overlay if the user wants brainstorming help.
    - Appends the collaborative overlay if working with other developers.
    - Remaps ARCHITECTURE → PRD_ARCHITECTURE for standard-tier collaborative projects.
    """
    # Load base workflow
    complexity = answers["complexity"]
    base = _load_yaml(f"{complexity}.yaml")
    steps: list[dict[str, Any]] = list(base["steps"])

    # Prepend brainstorm step if requested
    if answers.get("brainstorm") == "yes":
        overlay = _load_yaml("overlay_brainstorm.yaml")
        steps = list(overlay["steps"]) + steps

    # Swap to hierarchical task prompt for Complex when requested
    if complexity == "complex" and answers.get("hierarchical_tasks") == "yes":
        for step in steps:
            if step.get("id") == "tasks":
                step["prompt_file"] = "tasks_hierarchical.md"
                step["name"] = "Hierarchical Task Breakdown"
                break

    # Append collaborative steps if needed
    if answers.get("collaboration") == "collaborative":
        overlay = _load_yaml("overlay_collaborative.yaml")
        collab_steps = list(overlay["steps"])

        # For standard tier, the stored variable is PRD_ARCHITECTURE, not ARCHITECTURE.
        # Remap any references to ARCHITECTURE in the collaborative overlay.
        if complexity == "standard":
            mapping = {"ARCHITECTURE": "PRD_ARCHITECTURE"}
            collab_steps = _remap_injects(collab_steps, mapping)

        steps.extend(collab_steps)

    return steps
