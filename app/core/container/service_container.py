"""
Conclik Service Container
"""

from app.core.container.service_registry import service_registry


class ServiceContainer:

    def register(self, name: str, service):

        service_registry.register(name, service)

    def resolve(self, name: str):

        return service_registry.get(name)


service_container = ServiceContainer()

