"""Rich console formatting helpers for the workflow CLI."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def show_header(title: str) -> None:
    """Display the application title banner."""
    console.print()
    console.print(
        Panel(
            Text(title, justify="center", style="bold cyan"),
            border_style="cyan",
            padding=(1, 4),
        )
    )
    console.print()


QUIT_INPUTS = frozenset(("q", "quit", "cancel", "/cancel"))
BACK_CANCEL_OPTIONS = frozenset(("back", "back to main menu", "cancel"))


def show_menu(title: str, options: list[str], *, allow_quit: bool = True) -> int:
    """Display numbered options and return the selected option number (1-indexed).
    When allow_quit is True, returns 0 if the user enters q (cancel), unless the
    last option is already Back/Cancel (then only the number goes back).
    Re-prompts on invalid input; never crashes.
    """
    last_is_back = (
        bool(options)
        and options[-1].strip().lower() in BACK_CANCEL_OPTIONS
    )
    effective_allow_quit = allow_quit and not last_is_back

    body = "\n".join(f"  [bold][{i + 1}][/bold] {opt}" for i, opt in enumerate(options))
    if effective_allow_quit:
        body += "\n  [dim]q = cancel[/dim]"
    console.print(Panel(
        body,
        title=title,
        border_style="cyan",
        padding=(1, 2),
    ))

    while True:
        try:
            raw = console.input("[bold cyan]> [/bold cyan]").strip()
            if effective_allow_quit and raw.lower() in QUIT_INPUTS:
                return 0
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice
        except (ValueError, EOFError):
            pass
        msg = f"Please enter a number between 1 and {len(options)}."
        if effective_allow_quit:
            msg += " (q = cancel)"
        console.print(f"[red]{msg}[/red]")


def show_step(step_number: int, total_steps: int, step_name: str, target_tool: str) -> None:
    """Display a workflow step header."""
    console.print()
    console.rule(style="bright_yellow")
    console.print(
        f"  [bold bright_yellow]Step {step_number} of {total_steps}:[/bold bright_yellow] "
        f"[bold]{step_name}[/bold]"
    )
    console.print(f"  [dim]Paste into:[/dim] [italic]{target_tool}[/italic]")
    console.rule(style="bright_yellow")
    console.print()


def show_success(message: str) -> None:
    """Green checkmark + message."""
    console.print(f"  [green]✓[/green] {message}")


def show_error(message: str) -> None:
    """Red X + message."""
    console.print(f"  [red]✗[/red] {message}")


def show_info(message: str) -> None:
    """Info-styled message."""
    console.print(f"  [blue]ℹ[/blue] {message}")


def get_input(prompt_text: str, nav_hint: str | None = None) -> str:
    """Styled single-line input prompt. If nav_hint is set, show it in dim after the prompt."""
    if nav_hint:
        return console.input(f"[bold]{prompt_text}[/bold] [dim]{nav_hint}[/dim] [cyan]>[/cyan] ").strip()
    return console.input(f"[bold]{prompt_text}[/bold] [cyan]>[/cyan] ").strip()


def get_multiline_input(
    prompt_text: str,
    nav_hint: str | None = None,
    single_line_commands: set[str] | frozenset[str] | None = None,
) -> str:
    """Capture multi-line input. User presses Enter twice (two consecutive empty lines) to finish.
    If nav_hint is set, show it with 'Enter twice to finish' on separate lines in a dim block.
    If single_line_commands is set, only the first line is checked; when it matches (stripped, lowercased), it returns immediately."""
    if nav_hint:
        dim_part = f"Enter twice to finish\n{nav_hint}"
    else:
        dim_part = "Enter twice to finish"
    console.print(f"[bold]{prompt_text}[/bold]")
    console.print(f"[dim]({dim_part})[/dim]")
    lines: list[str] = []
    empty_count = 0
    commands = single_line_commands if single_line_commands is not None else set()

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            empty_count += 1
            if empty_count >= 2:
                break
            lines.append(line)
        else:
            empty_count = 0
            if commands and not lines and line.strip().lower() in commands:
                return line.strip()
            lines.append(line)

    # Strip trailing empty lines that were part of the termination signal
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


def confirm(question: str) -> bool:
    """Y/n confirmation prompt. Returns True for yes, False for no."""
    while True:
        answer = console.input(f"[bold]{question}[/bold] [dim](Y/n)[/dim] [cyan]>[/cyan] ").strip().lower()
        if answer in ("y", "yes", ""):
            return True
        if answer in ("n", "no"):
            return False
        console.print("[red]Please enter Y or N.[/red]")
