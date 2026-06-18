from config import os, snap_dir, snapshots_dir, metadata_default
import json

def init():
    
    # Snap directory creation
    if os.path.exists(snap_dir):
        print("Project already initialized.")
        return

    os.makedirs(snapshots_dir)

    with open(f"{snap_dir}/metadata.json", "w") as file:
        json.dump(metadata_default, file, indent=4)


    print("Project initialized successfully!")