import json
import os

class Settings:
    FILE_NAME = "settings.json"

    DEFAULTS = {
        "default_priority": 3,
        "auto_sort": False,
        "storage_file": "tasks.json"
    }

    def __init__(self):
        self.config = self.load()

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            self.save(self.DEFAULTS)
            return self.DEFAULTS.copy()

        with open(self.FILE_NAME, "r") as f:
            return json.load(f)

    def save(self, data=None):
        if data:
            self.config = data

        with open(self.FILE_NAME, "w") as f:
            json.dump(self.config, f, indent=4)

    def update(self, key, value):
        self.config[key] = value
        self.save()

    def get(self, key):
        return self.config.get(key, self.DEFAULTS.get(key))