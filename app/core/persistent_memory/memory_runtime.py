from app.core.persistent_memory.memory_storage import memory_storage


class MemoryRuntime:

    async def remember(self, key, value):
        await memory_storage.save(key, value)
        return True

    async def recall(self, key):
        return await memory_storage.load(key)


memory_runtime = MemoryRuntime()
