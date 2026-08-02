"""
Event Bus V2
"""

from collections import deque


class EventBus:

    def __init__(self):

        self.queue = deque()
        self.history = set()


    async def publish(self, event):

        if event.event_id in self.history:
            return {
                "status": "duplicate_event",
                "event_id": event.event_id,
            }

        self.queue.append(event)

        return {
            "status": "published",
            "event_id": event.event_id,
        }


    async def consume(self):

        if self.queue:

            return self.queue.popleft()

        return None


    async def clear(self):

        self.queue.clear()
        self.history.clear()


event_bus = EventBus()
