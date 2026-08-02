"""
Event Record V1
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class EventRecord:

    event_id: str

    event_type: str

    source: str

    payload: dict[str, Any]

    status: str

    created_at: datetime


    def to_dict(self):

        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "source": self.source,
            "payload": self.payload,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }
