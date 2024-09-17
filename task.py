# task.py

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status}"
