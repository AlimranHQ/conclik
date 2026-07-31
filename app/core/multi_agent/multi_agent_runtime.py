from app.core.multi_agent.multi_agent_planner import multi_agent_planner


class MultiAgentRuntime:

    async def run(self, tasks):

        assignments = await multi_agent_planner.assign(tasks)

        return {
            "assignments": assignments,
            "total_agents": len(assignments),
        }


multi_agent_runtime = MultiAgentRuntime()
