from datetime import datetime


class EventTrace:

    def __init__(self):

        self.history = []

    async def record(self, event):

        self.history.append(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "type": event.type,
                "source": event.source,
                "payload": event.payload,
            }
        )

    async def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    async def all(self):

        return self.history

    async def count(self):

        return len(self.history)

    async def clear(self):

        self.history.clear()


event_trace = EventTrace()
