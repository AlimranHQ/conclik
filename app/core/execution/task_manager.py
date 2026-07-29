"""
Task Manager
"""

from app.core.execution.task_queue import task_queue


class TaskManager:

    def submit(self, task):
        task_queue.push(task)

    def next(self):
        return task_queue.pop()


task_manager = TaskManager()

