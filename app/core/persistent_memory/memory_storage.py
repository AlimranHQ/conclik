class MemoryStorage:

    def __init__(self):
        self._memory = {}

    async def save(self, key, value):
        self._memory[key] = value

    async def load(self, key):
        return self._memory.get(key)

    async def all(self):
        return self._memory


memory_storage = MemoryStorage()
