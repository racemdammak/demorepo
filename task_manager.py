from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = Storage.load()

    def add_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        self.tasks.append(task)
        Storage.save(self.tasks)

    def list_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            Storage.save(self.tasks)

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            Storage.save(self.tasks)

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower()]

    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)
        Storage.save(self.tasks)