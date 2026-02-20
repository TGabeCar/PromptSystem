"""Prompt user to choose or create a project folder (file explorer or path input)."""

from __future__ import annotations

from pathlib import Path

from app.display import get_input


def get_project_directory() -> Path | None:
    """Ask the user to choose or create a project folder.

    Tries tkinter folder picker first. On failure or empty selection,
    falls back to text prompt. Returns resolved Path, or None if skipped/cancelled.
    """
    path_str: str | None = None

    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError:
        pass
    else:
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        path_str = filedialog.askdirectory(
            title="Choose or create project folder",
            mustexist=False,
        )
        try:
            root.destroy()
        except Exception:
            pass

    if not path_str or not path_str.strip():
        path_str = get_input(
            "Project folder path (or leave empty to skip):",
            nav_hint="Folder will be created if it does not exist",
        )

    if not path_str or not path_str.strip():
        return None

    target = Path(path_str.strip()).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    return target
