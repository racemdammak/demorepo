import json
import os
import hashlib

FILE_PATH = "inventory.json"


def load_inventory():
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r") as f:
            content = json.load(f)
        return content.get("items", {})
    except (json.JSONDecodeError, ValueError):
        print("Warning: inventory.json is corrupted. Resetting inventory.")
        return {}
    except OSError as e:
        print(f"Error accessing inventory file: {e}")
        return {}

# this is our legacy code unit
def generate_inventory_checksum(data):
    """
    Generates checksum for integrity validation.
    (Sensitive legacy function candidate)
    """
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.md5(encoded).hexdigest()


def save_inventory(data):
    """
    Critical persistence function.
    """
    try:
        checksum = generate_inventory_checksum(data)

        payload = {
            "checksum": checksum,
            "items": data
        }

        with open(FILE_PATH, "w") as f:
            json.dump(payload, f, indent=4)

    except OSError as e:
        print(f"Error saving inventory file: {e}")