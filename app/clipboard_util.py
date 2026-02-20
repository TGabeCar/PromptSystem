"""Clipboard copy with fallback for long prompts (e.g. Windows Clipboard History issues)."""

from __future__ import annotations

import tempfile
import time


def copy_prompt_to_clipboard_or_file(text: str) -> tuple[bool, str | None]:
    """Copy text to clipboard. On failure (e.g. long text + Windows Clipboard History), save to a temp file.

    Returns:
        (True, None) on success.
        (False, path) on failure; path is the temp file where the prompt was saved.
    """
    try:
        import pyperclip
        pyperclip.copy(text)
        return True, None
    except Exception:
        pass

    # One retry after a short delay (OpenClipboard can be temporarily busy)
    time.sleep(0.4)
    try:
        import pyperclip
        pyperclip.copy(text)
        return True, None
    except Exception:
        pass

    # Fallback: write to temp file so user can open and copy manually
    try:
        fd, path = tempfile.mkstemp(suffix=".txt", prefix="prompt_saved_")
        with open(fd, "w", encoding="utf-8") as f:
            f.write(text)
        return False, path
    except OSError:
        return False, None
