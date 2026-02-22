"""Clipboard copy with fallback for long prompts (e.g. Windows Clipboard History issues)."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile


def _copy_via_powershell(text: str) -> bool:
    """Copy text to clipboard via PowerShell's Set-Clipboard. Windows-only.

    Writes text to a temp file, then calls powershell.exe to read and Set-Clipboard.
    This delegates clipboard locking to a separate process, avoiding the OpenClipboard
    contention caused by Windows Clipboard History on long text.
    """
    fd, tmp = tempfile.mkstemp(suffix=".txt", prefix="clip_")
    try:
        with open(fd, "w", encoding="utf-8") as f:
            f.write(text)
        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                f'Set-Clipboard (Get-Content -Raw -Encoding UTF8 "{tmp}")',
            ],
            capture_output=True,
            timeout=10,
        )
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def _copy_via_pyperclip(text: str) -> bool:
    """Copy using pyperclip. Used as fallback on non-Windows or if PowerShell path fails."""
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def copy_prompt_to_clipboard_or_file(text: str) -> tuple[bool, str | None]:
    """Copy text to clipboard. On failure, save to a temp file for manual copy.

    On Windows, delegates to PowerShell's Set-Clipboard (avoids OpenClipboard contention
    with Clipboard History). Falls back to pyperclip, then to a temp file.

    Returns:
        (True, None) on success.
        (False, path) on failure; path is the temp file where the prompt was saved.
    """
    if sys.platform == "win32":
        if _copy_via_powershell(text):
            return True, None
        if _copy_via_pyperclip(text):
            return True, None
    else:
        if _copy_via_pyperclip(text):
            return True, None

    # Final fallback: write to temp file so user can open and copy manually
    try:
        fd, path = tempfile.mkstemp(suffix=".txt", prefix="prompt_saved_")
        with open(fd, "w", encoding="utf-8") as f:
            f.write(text)
        return False, path
    except OSError:
        return False, None
