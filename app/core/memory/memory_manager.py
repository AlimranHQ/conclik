"""
Conclik Memory Manager
"""

from app.core.memory.memory_store import memory_store


class MemoryManager:

    def save(self, key: str, value):
        memory_store.save(key, value)

    def load(self, key: str):
        return memory_store.load(key)


memory_manager = MemoryManager()

