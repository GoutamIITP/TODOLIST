# task_manager.py
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_title, new_status):
        for task in self.tasks:
            if task.title == task_title:
                task.status = new_status
                break

    def list_tasks(self):
        for task in self.tasks:
            print(task)
