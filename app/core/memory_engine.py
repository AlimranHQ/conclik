"""
Conclik Pilot AI
Version : 4.3.0
Module  : Memory Engine
"""

from typing import Dict, Any


class MemoryEngine:

    def __init__(self):
        self.memory: Dict[str, Any] = {}

    def save(self, key: str, value: Any):
        self.memory[key] = value

    def load(self, key: str):
        return self.memory.get(key)

    def delete(self, key: str):
        if key in self.memory:
            del self.memory[key]

    def clear(self):
        self.memory.clear()

    def all(self):
        return self.memory


memory_engine = MemoryEngine()
