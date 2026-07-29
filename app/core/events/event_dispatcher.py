"""
Event Dispatcher
"""

from app.core.events.event_queue import event_queue


class EventDispatcher:

    def dispatch(self):

        while True:

            event = event_queue.pop()

            if event is None:
                break

            print(f"[EVENT] {event.name} <- {event.source}")


event_dispatcher = EventDispatcher()

