from snapshot.config import snap_dir, os
from snapshot.utils.metadata_loader import load_metadata
from snapshot.utils.console import (
    console, error, info, print_header,
    PRIMARY, SUCCESS, MUTED, INFO,
)
from rich.table import Table
from rich.panel import Panel

def list_snap():
    if not os.path.exists(snap_dir):
        error("Project not initialized. Run [bold]snap init[/bold] first.")
        return

    metadata = load_metadata()
    snapshots = metadata["snapshots"]

    print_header()

    if not snapshots:
        info("No snapshots found. Run [bold]snap save <message>[/bold] to create one.")
        return

    table = Table(
        show_header=True,
        header_style=f"bold {PRIMARY}",
        border_style=MUTED,
        padding=(0, 2),
        show_edge=False,
        show_lines=True,
        row_styles=["", "dim"],
    )

    table.add_column("#",            style=f"bold {PRIMARY}", justify="right", min_width=4)
    table.add_column("Message",      style="bold white",      min_width=20)
    table.add_column("Created",      style=INFO,              min_width=20)
    table.add_column("Archive Path", style=MUTED,             min_width=16)

    for snap in snapshots:
        # Truncate the datetime for cleaner display
        created = snap["created_on"][:19]
        table.add_row(
            str(snap["save_id"]),
            snap["snap_message"],
            created,
            snap.get("file", "—"),
        )

    console.print(
        Panel(
            table,
            title=f"[bold {PRIMARY}]Snapshots[/bold {PRIMARY}]",
            subtitle=f"[dim]{len(snapshots)} snapshot{'s' if len(snapshots) != 1 else ''}[/dim]",
            border_style=MUTED,
            padding=(1, 1),
        )
    )
    console.print()
