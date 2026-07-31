class ContextRuntime:

    def __init__(self):
        self._context = {}

    async def set(self, key, value):
        self._context[key] = value
        return True

    async def get(self, key):
        return self._context.get(key)

    async def all(self):
        return self._context


context_runtime = ContextRuntime()
