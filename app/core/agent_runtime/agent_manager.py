"""
Conclik Agent Manager V5
"""

from app.core.agent_runtime.agent_registry import agent_registry


class AgentManager:

    def register(self, name: str, agent):
        agent_registry.register(name, agent)
        return agent

    def unregister(self, name: str):
        agents = agent_registry.all()
        if name in agents:
            del agents[name]

    def load(self, name: str):
        return agent_registry.get(name)

    def exists(self, name: str):
        return self.load(name) is not None

    def list_agents(self):
        return list(agent_registry.all().keys())


agent_manager = AgentManager()
