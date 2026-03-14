import json


def load_tasks(file_path):
    """
    Load tasks from JSON file.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(file_path, tasks):
    """
    Save tasks to JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)