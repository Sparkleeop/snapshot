from config import snap_dir, os
from utils.metadata_loader import load_metadata

def list_snap():
    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return
    
    metadata = load_metadata()

    for snapshot in metadata["snapshots"]:
        print("-" * 20)
        print(f"Snap Message: {snapshot['snap_message']}")
        print(f"Snap ID: {snapshot['save_id']}")
        print(f"Created On: {snapshot['created_on']}")
        print("-" * 20)