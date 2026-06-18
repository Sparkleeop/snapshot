from config import *
from utils.file_manager import unzip_dir, clear_contents
from utils.metadata_loader import load_metadata
from utils.console import (
    console, success, error, warning, info,
    PRIMARY, WARNING, ERROR, MUTED,
)
from rich.panel import Panel
from rich.prompt import Confirm

def restore(snap_id, clean=False):
    if not os.path.exists(snap_dir):
        error("Project not initialized. Run [bold]snap init[/bold] first.")
        return

    metadata = load_metadata()

    snapshot = next(
        (item for item in metadata["snapshots"] if item["save_id"] == snap_id),
        None,
    )

    if snapshot is None:
        error(f"Snapshot [bold]#{snap_id}[/bold] not found.")
        return


    console.print()
    info(f"Snapshot [bold]#{snapshot['save_id']}[/bold] — \"{snapshot['snap_message']}\"")
    info(f"Created: {snapshot['created_on'][:19]}")
    console.print()


    if clean:
        console.print(
            Panel(
                "[bold]This is a clean restore.[/bold]\n"
                "All current project files will be [bold]permanently deleted[/bold]\n"
                "before extracting the snapshot.",
                title="[bold]!  Destructive Operation[/bold]",
                title_align="left",
                border_style=WARNING,
                padding=(1, 2),
            )
        )
    else:
        warning(
            "Restoring will overwrite any conflicting files in the project directory."
        )

    console.print()


    confirmed = Confirm.ask(
        f"  [{PRIMARY}]Restore snapshot #{snap_id}?[/{PRIMARY}]",
        default=False,
    )

    if not confirmed:
        info("Restore cancelled.")
        return


    with console.status(
        f"[{PRIMARY}]  Restoring snapshot #{snap_id}…[/{PRIMARY}]",
        spinner="dots",
        spinner_style=PRIMARY,
    ):
        if clean:
            clear_contents(current_dir)

        zip_path = snapshot["file"]
        unzip_dir(zip_path)

    success(f"Snapshot [bold]#{snap_id}[/bold] restored successfully!")
