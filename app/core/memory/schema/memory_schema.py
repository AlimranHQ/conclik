from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class MemoryRecord:

    goal: str

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    workflow: Dict[str, Any] = field(default_factory=dict)

    reflection: Dict[str, Any] = field(default_factory=dict)

    learning: Dict[str, Any] = field(default_factory=dict)

    adaptive: Dict[str, Any] = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)
