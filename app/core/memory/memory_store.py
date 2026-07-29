"""
Conclik Memory Store
"""

class MemoryStore:

    def __init__(self):
        self._store = {}

    def save(self, key: str, value):
        self._store[key] = value

    def load(self, key: str):
        return self._store.get(key)

    def all(self):
        return self._store


memory_store = MemoryStore()

