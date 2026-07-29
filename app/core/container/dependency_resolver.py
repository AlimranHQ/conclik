"""
Dependency Resolver
"""

from app.core.container.service_container import service_container


class DependencyResolver:

    def resolve(self, service_name: str):

        return service_container.resolve(service_name)


dependency_resolver = DependencyResolver()

