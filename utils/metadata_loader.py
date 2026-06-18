from config import *
import json


def load_metadata():
    with open(f"{snap_dir}/metadata.json", "r") as file:
        return json.load(file)
    
def save_metadata(data):
    with open(f"{snap_dir}/metadata.json", "w") as file:
        json.dump(data, file, indent=4)