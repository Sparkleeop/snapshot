from config import *
from fnmatch import fnmatch

def load_ignore_patterns():
    snap_ignore_file = f"{current_dir}/.snapignore"

    if not os.path.exists(snap_ignore_file):
        return []

    with open(snap_ignore_file, "r") as file:
        patterns = file.readlines()

    return [
        line.strip()
        for line in patterns
        if line.strip() and not line.strip().startswith("#")
    ]

def should_ignore(file_path, ignore_patterns):
    relative_path = os.path.relpath(file_path, current_dir)
    relative_path = relative_path.replace("\\", "/")

    for pattern in ignore_patterns:
        pattern = pattern.strip()

        # Folder ignore
        if pattern.endswith("/"):
            folder = pattern.rstrip("/")
            if relative_path.startswith(folder + "/"):
                return True

        # Wildcard/file ignore
        if fnmatch(relative_path, pattern):
            return True

    return False