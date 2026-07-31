from app.core.agent_registry.agent_registry import list_agents, get_agent


class AgentPool:

    async def load(self):

        pool = {}

        for name in list_agents():

            agent = get_agent(name)

            if agent is not None:
                pool[name] = agent

        return {
            "status": "pool_ready",
            "total_agents": len(pool),
            "agents": pool,
        }


agent_pool = AgentPool()
