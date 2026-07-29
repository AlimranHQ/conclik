"""
Conclik Workflow
"""

from dataclasses import dataclass, field


@dataclass
class Workflow:

    name: str

    tasks: list = field(default_factory=list)

