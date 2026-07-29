from dataclasses import dataclass
from typing import Any

@dataclass
class ProjectResult:
    success: bool
    data: Any = None
    message: str = ""
