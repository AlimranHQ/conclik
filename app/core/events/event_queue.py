"""
Event Queue
"""

from collections import deque


class EventQueue:

    def __init__(self):

        self.queue = deque()

    def push(self, event):

        self.queue.append(event)

    def pop(self):

        if self.queue:

            return self.queue.popleft()

        return None


event_queue = EventQueue()

