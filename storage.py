import json
from pathlib import Path

FILE_PATH = Path("notes.json")


def load_notes():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_notes(notes):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)