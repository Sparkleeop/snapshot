from config import *
from utils.snapignore import load_ignore_patterns, should_ignore
import zipfile, shutil
from pathlib import Path

SYSTEM_PRESERVE = {
    ".snap",
    ".git"
}

def zip_dir(dir_path, zip_name):

    ignore_patterns = load_ignore_patterns()

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_path):
            dirs[:] = [d for d in dirs if d != ".snap"]
            dirs[:] = [d for d in dirs if d != ".git"]
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path, ignore_patterns):
                    continue
                # arcname preserves directory structure relative to dir_path
                arcname = os.path.relpath(file_path, start=dir_path)
                zipf.write(file_path, arcname)

def unzip_dir(zip_path):
    # Extract all files to a directory
    with zipfile.ZipFile(f'{zip_path}', 'r') as zip_ref:
        zip_ref.extractall(current_dir)

def clear_contents(dir_path):
    folder = Path(dir_path)

    for item in folder.iterdir():

        if item.name in SYSTEM_PRESERVE:
            continue

        if item.is_file() or item.is_symlink():
            item.unlink()

        elif item.is_dir():
            shutil.rmtree(item)

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip symbolic links to avoid infinite loops or errors
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size