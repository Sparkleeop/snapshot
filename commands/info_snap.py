from config import *
from utils.metadata_loader import load_metadata
from utils.console import (
    console,
    error,
    info,
    PRIMARY, INFO, MUTED,
)
from rich.panel import Panel


def show_info(snap_id):
    if not os.path.exists(snap_dir):
        error("Project not initialized. Run [bold]snap init[/bold] first.")
        return

    metadata = load_metadata()

    snapshot = next(
        (
            item
            for item in metadata["snapshots"]
            if item["save_id"] == snap_id
        ),
        None,
    )

    if snapshot is None:
        error(f"Snapshot [bold]#{snap_id}[/bold] not found.")
        return

    console.print()
    console.print(
        Panel(
            f"[bold]Message:[/bold]  [{INFO}]{snapshot['snap_message']}[/{INFO}]\n"
            f"[bold]Created:[/bold]  [{INFO}]{snapshot['created_on'][:19]}[/{INFO}]\n"
            f"[bold]Archive:[/bold]  [{MUTED}]{snapshot['file']}[/{MUTED}]",
            title=f"[bold {PRIMARY}]Snapshot #{snapshot['save_id']}[/bold {PRIMARY}]",
            border_style=MUTED,
            padding=(1, 2),
            expand=False,
        )
    )
    console.print()