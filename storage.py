import json
import os

FILE_PATH = "users.json"


def load_users():
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        print("Warning: Corrupted users.json file. Resetting.")
        return {}

    with open(FILE_PATH, "r") as f:
        return json.load(f)  # BUG: no error handling


def save_users(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)