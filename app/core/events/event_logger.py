"""
Event Logger
"""

class EventLogger:

    def log(self, event):

        print(f"[LOG] {event.name}")


event_logger = EventLogger()

