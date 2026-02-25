from task import Task
from storage import Storage
from settings import Settings

class TaskManager:
    def __init__(self):
        self.settings = Settings()
        self.storage = Storage()
        self.tasks = self.storage.load()

    def add_task(self, title, description="", priority=None):
        if priority is None:
            priority = self.settings.get("default_priority")

        task = Task(title, description, priority)
        self.tasks.append(task)

        if self.settings.get("auto_sort"):
            self.sort_by_priority(save=False)

        self.storage.save(self.tasks)

    def list_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.storage.save(self.tasks)

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.storage.save(self.tasks)

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower()]

    def sort_by_priority(self, save=True):
        self.tasks.sort(key=lambda task: task.priority)
        if save:
            self.storage.save(self.tasks)