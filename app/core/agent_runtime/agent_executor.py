"""
Agent Executor
"""

class AgentExecutor:

    async def execute(self, agent, *args, **kwargs):

        if hasattr(agent, "run"):
            return await agent.run(*args, **kwargs)

        raise RuntimeError("Agent has no run() method")


agent_executor = AgentExecutor()

