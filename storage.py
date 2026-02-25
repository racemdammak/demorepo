import json
import os

class Storage:
    FILE_NAME = "tasks.json"

    @classmethod
    def save(cls, tasks): # legacy code
        with open(cls.FILE_NAME, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    @classmethod
    def load(cls):
        if not os.path.exists(cls.FILE_NAME):
            return []

        with open(cls.FILE_NAME, "r") as f:
            data = json.load(f)
            from task import Task
            return [Task.from_dict(item) for item in data]