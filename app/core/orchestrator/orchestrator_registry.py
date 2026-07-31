class OrchestratorRegistry:

    def __init__(self):
        self._tasks = {}

    def register(self, name, runtime):
        self._tasks[name] = runtime

    def get(self, name):
        return self._tasks.get(name)

    def all(self):
        return self._tasks


orchestrator_registry = OrchestratorRegistry()
