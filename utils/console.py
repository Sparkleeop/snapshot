

from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import sys, io


if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


PRIMARY   = "#3B82F6"
SUCCESS   = "#10B981"
WARNING   = "#F59E0B"
ERROR     = "#EF4444"
INFO      = "#06B6D4"
MUTED     = "#6B7280"


snap_theme = Theme({
    "primary":  PRIMARY,
    "success":  f"bold {SUCCESS}",
    "warning":  f"bold {WARNING}",
    "error":    f"bold {ERROR}",
    "info":     INFO,
    "muted":    MUTED,
    "header":   f"bold {PRIMARY}",
})

console = Console(theme=snap_theme)



def success(message: str) -> None:

    console.print(f"  [success]+[/success]  {message}")

def error(message: str) -> None:

    console.print(f"  [error]x[/error]  [error]{message}[/error]")

def warning(message: str) -> None:

    console.print(f"  [warning]![/warning]  [warning]{message}[/warning]")

def info(message: str) -> None:

    console.print(f"  [info]>[/info]  [info]{message}[/info]")



SNAP_LOGO = Text.from_markup(
    f"[bold {PRIMARY}]Snap[/bold {PRIMARY}]  [dim]- Local Project Snapshots[/dim]"
)

def print_header() -> None:

    console.print()
    console.print(
        Panel(
            SNAP_LOGO,
            border_style=PRIMARY,
            padding=(0, 2),
        )
    )
    console.print()



def print_help() -> None:

    print_header()

    table = Table(
        show_header=True,
        header_style=f"bold {PRIMARY}",
        border_style=MUTED,
        padding=(0, 2),
        show_edge=False,
        show_lines=False,
    )
    table.add_column("Command", style="bold white", min_width=28)
    table.add_column("Description", style="dim")

    table.add_row("snap init",                    "Initialize a new Snap project")
    table.add_row("snap save <message>",          "Save a snapshot with a message")
    table.add_row("snap list",                    "List all saved snapshots")
    table.add_row("snap restore <id>",            "Restore a snapshot by ID")
    table.add_row("snap restore <id> --clean",    "Restore & remove current files first")

    console.print(
        Panel(
            table,
            title=f"[bold {PRIMARY}]Available Commands[/bold {PRIMARY}]",
            border_style=MUTED,
            padding=(1, 1),
        )
    )
    console.print()