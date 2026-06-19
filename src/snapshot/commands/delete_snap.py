from snapshot.config import snap_dir, os
from snapshot.utils.metadata_loader import load_metadata, save_metadata
from snapshot.utils.console import (
    console, success, error, warning, info,
    PRIMARY, WARNING, ERROR, MUTED,
)
from rich.panel import Panel
from rich.prompt import Confirm

def delete(snap_id):
    if not os.path.exists(snap_dir):
        error("Project not initialized.")
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
        error(f"Snapshot #{snap_id} not found.")
        return
    
    console.print(
        Panel(
            "[bold]This will permanently delete the selected snapshot.[/bold]\n"
            "The snapshot archive and its metadata entry will be removed.",
            title="[bold]! Snapshot Deletion[/bold]",
            title_align="left",
            border_style=WARNING,
            padding=(1, 2),
        )
    )
    console.print()

    confirmed = Confirm.ask(
        f"Delete snapshot #{snap_id}?",
        default=False,
    )

    if not confirmed:
        info("Deletion cancelled.")
        return

    zip_path = snapshot["file"]

    if os.path.exists(zip_path):
        os.remove(zip_path)

    metadata["snapshots"] = [
        item
        for item in metadata["snapshots"]
        if item["save_id"] != snap_id
    ]

    save_metadata(metadata)

    success(f"Deleted snapshot #{snap_id}")
