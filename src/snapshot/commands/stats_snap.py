from snapshot.config import snap_dir, os
from snapshot.utils.metadata_loader import load_metadata
from snapshot.utils.file_manager import get_directory_size, human_size

from snapshot.utils.console import (
    console,
    error,
    PRIMARY,
    MUTED,
)
from rich.table import Table
from rich.panel import Panel

def stats():

    if not os.path.exists(snap_dir):
        error("Project not initialized. Run [bold]snap init[/bold] first.")
        return

    metadata = load_metadata()
    snapshots = metadata["snapshots"]

    snap_count = len(snapshots)
    snap_size = get_directory_size(snap_dir)

    latest_snap = snapshots[-1] if snapshots else None
    oldest_snap = snapshots[0] if snapshots else None

    table = Table(
        show_header=True,
        header_style=f"bold {PRIMARY}",
        border_style=MUTED,
        padding=(0, 2),
        show_edge=False,
        show_lines=True,
    )

    table.add_column("Metric", style=f"bold {PRIMARY}")
    table.add_column("Value", style="bold white")

    table.add_row(
        "Total Snapshots",
        str(snap_count)
    )

    table.add_row(
        "Storage Used",
        human_size(snap_size)
    )

    if oldest_snap:
        table.add_row(
            "Oldest Snapshot",
            f"#{oldest_snap['save_id']}"
        )

    if latest_snap:
        table.add_row(
            "Latest Snapshot",
            f"#{latest_snap['save_id']}"
        )

        table.add_row(
            "Latest Message",
            latest_snap["snap_message"]
        )

        table.add_row(
            "Created",
            latest_snap["created_on"][:19]
        )

    console.print(
        Panel(
            table,
            title=f"[bold {PRIMARY}]Statistics[/bold {PRIMARY}]",
            subtitle=f"[dim]{snap_count} snapshot{'s' if snap_count != 1 else ''}[/dim]",
            border_style=MUTED,
            padding=(1, 1),
        )
    )

    console.print()
