"""
Master Router V1
"""

from app.core.master_orchestrator.master_registry import master_registry


class MasterRouter:

    def route(self, name):

        return master_registry.get(name)


master_router = MasterRouter()
