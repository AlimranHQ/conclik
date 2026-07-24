"""
Conclik v5.0
Task Queue
"""

from queue import Queue

task_queue = Queue()

def add_task(task: dict):
    task_queue.put(task)

def get_task():
    if task_queue.empty():
        return None
    return task_queue.get()

def size():
    return task_queue.qsize()
