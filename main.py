import os, zipfile, json, argparse
from datetime import datetime

current_dir = os.getcwd()
snap_dir = ".snap"
snapshots_dir = f"{snap_dir}/snapshots"

parser = argparse.ArgumentParser(prog="snap", description="Project snapshot manager")

metadata_default = {
    "snapshots": []
}

def init():
    
    # Snap directory creation
    if os.path.exists(snap_dir):
        print("Project already initialized.")
        return

    os.makedirs(snapshots_dir)

    with open(f"{snap_dir}/metadata.json", "w") as file:
        json.dump(metadata_default, file, indent=4)


    print("Project initialized successfully!")

def snapshot(snap_message):
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

    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return

def zip_dir(dir_path, zip_name):

    ignore_patterns = load_ignore_patterns()

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_path):
            dirs[:] = [d for d in dirs if d != ".snap"]
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path, ignore_patterns):
                    continue
                # arcname preserves directory structure relative to dir_path
                arcname = os.path.relpath(file_path, start=dir_path)
                zipf.write(file_path, arcname)

def load_metadata():
    with open(f"{snap_dir}/metadata.json", "r") as file:
        return json.load(file)
    
def save_metadata(data):
    with open(f"{snap_dir}/metadata.json", "w") as file:
        json.dump(data, file, indent=4)

def list_snap():
    metadata = load_metadata()

    for snapshot in metadata["snapshots"]:
        print("-" * 20)
        print(f"Snap Message: {snapshot['snap_message']}")
        print(f"Snap ID: {snapshot['save_id']}")
        print(f"Created On: {snapshot['created_on']}")
        print("-" * 20)

    if not os.path.exists(snap_dir):
        print("Project not initialized.")
        return

def load_ignore_patterns():
    snap_ignore_file = f"{current_dir}/.snapignore"

    if not os.path.exists(snap_ignore_file):
        return []

    with open(snap_ignore_file, "r") as file:
        patterns = file.readlines()

    patterns = [
        line.strip()
        for line in patterns
        if line.strip() and not line.startswith("#")
    ]

    return patterns

def should_ignore(file_path, ignore_patterns):
    normalized_path = file_path.replace("\\", "/")

    for pattern in ignore_patterns:
        if pattern in normalized_path:
            return True

    return False
    


subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("init")
subparsers.add_parser("list")
subparsers.add_parser("test")

save_parser = subparsers.add_parser("save")
save_parser.add_argument("message")

args = parser.parse_args()

if args.command == "init":
    init()

elif args.command == "save":
    snapshot(args.message)

elif args.command == "list":
    list_snap()

else:
    parser.print_help()