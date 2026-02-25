from datetime import datetime

class Task:
    def __init__(self, title, description="", priority=3, completed=False, created_at=None):
        self.title = title
        self.description = description
        self.priority = priority  # 1 (High) → 5 (Low)
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now().isoformat()

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data.get("description", ""),
            data.get("priority", 3),
            data.get("completed", False),
            data.get("created_at")
        )