"""
Conclik Service Registry
"""

class ServiceRegistry:

    def __init__(self):
        self._services = {}

    def register(self, name: str, service):
        self._services[name] = service

    def get(self, name: str):
        return self._services.get(name)

    def all(self):
        return self._services


service_registry = ServiceRegistry()

