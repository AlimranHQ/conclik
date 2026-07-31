class ExecutionRegistry:

    def __init__(self):
        self._executors = {}

    def register(self, name, executor):
        self._executors[name] = executor

    def get(self, name):
        return self._executors.get(name)


execution_registry = ExecutionRegistry()
