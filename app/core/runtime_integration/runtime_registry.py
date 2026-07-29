class RuntimeRegistry:

    def __init__(self):
        self._runtimes = {}

    def register(self, name, runtime):
        self._runtimes[name] = runtime

    def get(self, name):
        return self._runtimes.get(name)

    def all(self):
        return self._runtimes


runtime_registry = RuntimeRegistry()
