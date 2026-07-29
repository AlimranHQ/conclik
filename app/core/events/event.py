"""
Conclik Event
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Event:

    name: str

    source: str

    payload: dict

    timestamp: datetime


