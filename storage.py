import json
import os

FILE_PATH = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)  # BUG: no error handling


def save_expenses(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)