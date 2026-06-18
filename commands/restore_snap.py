from config import *
from utils.file_manager import unzip_dir, clear_contents
from utils.metadata_loader import load_metadata

def restore(snap_id, clean=False):
    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return
    
    metadata = load_metadata()

    snapshot = next((item for item in metadata["snapshots"] if item["save_id"] == snap_id), None)

    if snapshot is None:
        print("Snapshot not found.")
        return
    
    print(
        "WARNING: Clean restore "
        "will delete current project files."
    )
    answer = input(f"Restore snapshot {snap_id}? (y/n): ")

    if answer.lower() != "y":
        print("Cancelled.")
        return
    
    if clean:
        clear_contents(current_dir)
        
    zip_path = snapshot["file"]

    unzip_dir(zip_path)
    print("Restore complete.")

