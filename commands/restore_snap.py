from config import *
from utils.file_manager import unzip_dir
from utils.metadata_loader import load_metadata

def restore(snap_id):
    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return
    
    metadata = load_metadata()

    snapshot = next((item for item in metadata['snapshots'] if item['save_id'] == snap_id), None)

    if snapshot:
        print(f"Found: {snapshot['file']}")
    else:
        print("Snapshot not found.")
    
    zip_path = snapshot["file"]

    unzip_dir(zip_path)

