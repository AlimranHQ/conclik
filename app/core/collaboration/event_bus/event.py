"""
Collaboration Event Model V3
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Event:

    type: str

    source: str

    payload: dict

    timestamp: datetime = field(
        default_factory=datetime.utcnow
    )

    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    processed: bool = False


    @property
    def name(self):

        return self.type
