class AutonomousRegistry:

    def __init__(self):
        self._cores = {}

    def register(self, name, core):
        self._cores[name] = core

    def get(self, name):
        return self._cores.get(name)

    def all(self):
        return self._cores


autonomous_registry = AutonomousRegistry()
