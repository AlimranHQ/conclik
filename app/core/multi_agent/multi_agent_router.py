"""
Multi Agent Router V5
"""

import app.core.agents

from app.core.agent_runtime.agent_registry import agent_registry


class MultiAgentRouter:

    def route(self, agent_name):

        return agent_registry.get(agent_name)


multi_agent_router = MultiAgentRouter()
