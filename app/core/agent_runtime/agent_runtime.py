from app.core.runtime_tools.router.tool_router import tool_router


class AgentRuntime:

    async def execute(self, agent: str, task: str):

        if agent == "research_agent":

            return await tool_router.execute(
                "terminal",
                f"echo Research: {task}"
            )

        return {
            "status": "unknown_agent",
            "agent": agent,
        }


agent_runtime = AgentRuntime()
