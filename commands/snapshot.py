from config import snap_dir, current_dir, os, snapshots_dir
from utils.metadata_loader import save_metadata, load_metadata
from utils.file_manager import zip_dir
from datetime import datetime

def snapshot(snap_message):
    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return
    
    metadata = load_metadata()

    save_no = len(metadata["snapshots"]) + 1
    zip_path = f"{snapshots_dir}/{save_no}.zip"
    zip_dir(current_dir, zip_path)
    created_on = str(datetime.now())

    metadata["snapshots"].append({
        "snap_message": snap_message,
        "save_id": save_no,
        "file": zip_path,
        "created_on": created_on
    })

    save_metadata(metadata)
    print("Snapshot saved")