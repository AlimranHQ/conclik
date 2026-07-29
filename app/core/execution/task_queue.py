"""
Task Queue
"""

from collections import deque


class TaskQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, task):
        self.queue.append(task)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return None


task_queue = TaskQueue()

