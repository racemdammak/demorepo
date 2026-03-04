import json
import os

FILE_PATH = "keys.json"


def load_keys():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)  # BUG: No error handling


def save_keys(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)