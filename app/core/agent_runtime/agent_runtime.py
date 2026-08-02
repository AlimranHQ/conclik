"""
Conclik Agent Runtime V3
"""

import app.core.agents

from app.core.agent_runtime.agent_registry import agent_registry
from app.core.collaboration.workspace.shared_workspace import shared_workspace


class AgentRuntime:

    async def execute(self, agent: str, task: str):

        runtime_agent = agent_registry.get(agent)

        if runtime_agent is None:
            return {
                "status": "unknown_agent",
                "agent": agent,
                "task": task,
            }

        result = await runtime_agent.run(task)

        await shared_workspace.write(
            agent,
            result,
        )

        return result


agent_runtime = AgentRuntime()
