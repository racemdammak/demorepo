import json
import os

FILE_PATH = "inventory.json"


def load_inventory():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r") as f:
        # Hidden bug: no JSON error handling
        return json.load(f)  


def save_inventory(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)