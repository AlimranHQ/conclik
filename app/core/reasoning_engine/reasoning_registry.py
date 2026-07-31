class ReasoningRegistry:

    def __init__(self):
        self._engines = {}

    def register(self, name, engine):
        self._engines[name] = engine

    def get(self, name):
        return self._engines.get(name)

    def all(self):
        return self._engines


reasoning_registry = ReasoningRegistry()
