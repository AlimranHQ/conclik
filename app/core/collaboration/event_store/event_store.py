"""
Event Store V1
"""

from app.core.collaboration.event_store.event_record import EventRecord


class EventStore:

    def __init__(self):

        self.events = []


    async def save(self, event: EventRecord):

        self.events.append(event)

        return {
            "status": "stored",
            "event_id": event.event_id,
        }


    async def get(self, event_id: str):

        for event in self.events:

            if event.event_id == event_id:
                return event

        return None


    async def all(self):

        return self.events


    async def clear(self):

        self.events.clear()

        return {
            "status": "cleared"
        }


event_store = EventStore()
