"""
Conclik Pilot AI
Version : 4.3.0
Module : Memory Service
"""

from app.core.memory_engine import memory_engine


class MemoryService:

    def save(self, key, value):
        memory_engine.save(key, value)

    def load(self, key):
        return memory_engine.load(key)

    def clear(self):
        memory_engine.clear()


memory_service = MemoryService()
