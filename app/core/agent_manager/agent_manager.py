from app.core.agent_registry.agent_registry import get_agent


class AgentManager:

    async def execute(self, agent_name: str, goal: str):

        agent = get_agent(agent_name)

        if agent is None:
            return {
                "status": "unknown_agent",
                "agent": agent_name,
            }

        result = await agent.run(goal)

        return {
            "status": "completed",
            "agent": agent_name,
            "result": result,
        }


agent_manager = AgentManager()
