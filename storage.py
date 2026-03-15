import json


def load_books(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_books(file_path, books):
    with open(file_path, "w") as f:
        json.dump(books, f, indent=2)