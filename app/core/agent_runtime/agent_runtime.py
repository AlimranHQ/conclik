"""
Agent Runtime
Version: 2.0.0
"""

from app.core.agent_runtime.agent_manager import agent_manager
from app.core.agent_runtime.agent_executor import agent_executor


class AgentRuntime:

    async def run(self, agent_or_name, *args, **kwargs):

        if isinstance(agent_or_name, str):
            agent = agent_manager.load(agent_or_name)

            if agent is None:
                raise RuntimeError(
                    f"Unknown agent: {agent_or_name}"
                )
        else:
            agent = agent_or_name

        return await agent_executor.execute(
            agent,
            *args,
            **kwargs,
        )


agent_runtime = AgentRuntime()
