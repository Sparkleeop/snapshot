from config import os, snap_dir, snapshots_dir, metadata_default
from utils.console import success, warning
import json

def init():

    # Snap directory creation
    if os.path.exists(snap_dir):
        warning("Project already initialized.")
        return

    os.makedirs(snapshots_dir)

    with open(f"{snap_dir}/metadata.json", "w") as file:
        json.dump(metadata_default, file, indent=4)

    success("Project initialized successfully!")