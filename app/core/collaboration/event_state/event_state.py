"""
Event State Tracker V1
"""

from datetime import datetime, timezone
from enum import Enum


class EventStatus(str, Enum):

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    RETRYING = "retrying"



class EventStateTracker:


    def __init__(self):

        self.states = {}

        self.history = []



    async def create(self, event_id, status=EventStatus.PENDING):

        record = {
            "event_id": event_id,
            "status": status.value,
            "updated_at": datetime.now(timezone.utc),
        }

        self.states[event_id] = record

        self.history.append(record.copy())

        return record



    async def update(self, event_id, status):

        if event_id not in self.states:

            raise ValueError(
                f"Unknown event: {event_id}"
            )


        record = self.states[event_id]

        record["status"] = status.value

        record["updated_at"] = datetime.now(timezone.utc)


        self.history.append(
            record.copy()
        )

        return record



    async def get(self, event_id):

        return self.states.get(event_id)



    async def get_history(self):

        return self.history



    async def clear(self):

        self.states.clear()

        self.history.clear()


        return {
            "status": "cleared"
        }



event_state_tracker = EventStateTracker()
