"""
Agent Manager
"""

from app.core.agent_runtime.agent_registry import agent_registry


class AgentManager:

    def register(self, name: str, agent):
        agent_registry.register(name, agent)

    def load(self, name: str):
        return agent_registry.get(name)


agent_manager = AgentManager()

