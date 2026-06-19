from snapshot.config import snap_dir, os
from snapshot.utils.metadata_loader import load_metadata
from snapshot.commands.restore_snap import restore

from snapshot.utils.console import error

def restore_latest(is_clean=False):
    if not os.path.exists(snap_dir):
        error("Project not initialized. Run [bold]snap init[/bold] first.")
        return

    metadata = load_metadata()
    snapshots = metadata["snapshots"]

    if not snapshots:
        error("No snapshots found.")
        return

    latest_snap = snapshots[-1]
    
    restore(snap_id=latest_snap["save_id"], clean=is_clean)
