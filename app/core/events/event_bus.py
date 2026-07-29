"""
Event Bus
"""

from app.core.events.event_queue import event_queue


class EventBus:

    def publish(self, event):

        event_queue.push(event)


event_bus = EventBus()

