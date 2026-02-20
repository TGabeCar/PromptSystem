"""Multi-choice questionnaire for new project setup."""

from __future__ import annotations

import re
from typing import Any

from app.display import get_input, get_multiline_input, show_menu

# Questions and their mapped key values
QUESTIONS: dict[str, dict[str, Any]] = {
    "complexity": {
        "question": "Complexity level?",
        "options": [
            "Quick — under 1 day, simple script or automation",
            "Standard — 1-5 days, typical internal tool or dashboard",
            "Complex — 1+ weeks, multi-component or customer-facing",
        ],
        "keys": ["quick", "standard", "complex"],
    },
    "project_type": {
        "question": "Project type?",
        "options": [
            "General",
            "Automation / Script",
            "Internal Tool / Dashboard",
            "API / Backend Service",
            "Web Application",
            "Customer-Facing Product",
        ],
        "keys": ["general", "automation", "internal_tool", "api", "web_app", "customer_facing"],
    },
    "collaboration": {
        "question": "Working with other developers?",
        "options": [
            "Solo",
            "Collaborative",
        ],
        "keys": ["solo", "collaborative"],
    },
    "brainstorm": {
        "question": "Need help brainstorming the project description first?",
        "options": [
            "Yes — give me a brainstorm prompt first",
            "No — I already have my description ready",
        ],
        "keys": ["yes", "no"],
    },
    "hierarchical_tasks": {
        "question": "Task breakdown style?",
        "options": [
            "Single detailed list (default)",
            "Hierarchical (master plan + per-workstream task docs)",
        ],
        "keys": ["no", "yes"],
    },
}


def _slugify(name: str) -> str:
    """Convert a project name to a filesystem-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def run_questionnaire() -> dict[str, Any] | None:
    """Run the new-project questionnaire and return the answers dict."""
    answers: dict[str, Any] = {}

    # Project name
    while True:
        raw_name = get_input("Project name:")
        if raw_name:
            answers["name"] = _slugify(raw_name)
            break

    # Ask each multiple-choice question
    for key, q in QUESTIONS.items():
        if key == "hierarchical_tasks" and answers.get("complexity") != "complex":
            answers["hierarchical_tasks"] = "no"
            continue
        choice = show_menu(q["question"], q["options"])
        if choice == 0:
            return None
        answers[key] = q["keys"][choice - 1]

    # If user doesn't need brainstorming, capture project description now
    if answers["brainstorm"] == "no":
        desc = get_multiline_input("Please paste your project description:")
        answers["project_description"] = desc
    else:
        # User will provide a rough idea that gets refined in the brainstorm step
        desc = get_multiline_input("Give a rough description of your project idea:")
        answers["project_description"] = desc

    return answers
