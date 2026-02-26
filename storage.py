import json
import os

FILE_PATH = "inventory.json"


def load_inventory():
    """
    Loads inventory data from JSON file.
    Handles missing, corrupted, or inaccessible files safely.
    """
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        print("Warning: inventory.json is corrupted. Resetting inventory.")
        return {}
    except OSError as e:
        print(f"Error accessing inventory file: {e}")
        return {}


def save_inventory(data):
    """
    Saves inventory data to JSON file.
    """
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except OSError as e:
        print(f"Error saving inventory file: {e}")