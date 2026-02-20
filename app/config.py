"""Path constants and configuration for the workflow CLI."""

from pathlib import Path

# Root of the workflow-cli package (one level up from app/)
APP_ROOT: Path = Path(__file__).resolve().parent.parent

# Content directories
PROMPTS_DIR: Path = APP_ROOT / "prompts"
WORKFLOWS_DIR: Path = APP_ROOT / "workflows"
CURSOR_TEMPLATES_DIR: Path = APP_ROOT / "cursor_templates"
PROJECTS_DIR: Path = APP_ROOT / "projects"

# Ensure projects directory exists
PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
