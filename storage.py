import json

def load_tasks(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def save_tasks(file_path, tasks):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)