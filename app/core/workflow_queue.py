"""
Conclik Pilot AI
Version : 4.2.0
Module  : Workflow Queue
"""

from queue import Queue


class WorkflowQueue:

    def __init__(self):
        self.queue = Queue()

    def add(self, job):
        self.queue.put(job)

    def next(self):
        if self.queue.empty():
            return None
        return self.queue.get()

    def size(self):
        return self.queue.qsize()

    def empty(self):
        return self.queue.empty()


workflow_queue = WorkflowQueue()
