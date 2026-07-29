"""
Conclik Task
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:

    name: str
    payload: dict

    created_at: datetime = field(default_factory=datetime.now)

