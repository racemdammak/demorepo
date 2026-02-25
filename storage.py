import json
import os
from settings import Settings

class Storage:
    def __init__(self):
        self.settings = Settings()
        self.file_name = self.settings.get("storage_file")

    def save(self, tasks):
        with open(self.file_name, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self):
        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, "r") as f:
            data = json.load(f)
            from task import Task
            return [Task.from_dict(item) for item in data]