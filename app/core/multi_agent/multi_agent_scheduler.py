"""
Multi Agent Scheduler V6
"""


from app.core.multi_agent.multi_agent_executor import multi_agent_executor


class MultiAgentScheduler:


    async def schedule(self, assignments, goal):

        results = await multi_agent_executor.execute(
            assignments,
            goal
        )


        completed = [
            r["agent"]
            for r in results
            if r.get("status") == "completed"
        ]


        return {
            "status": "team_completed",
            "completed_agents": completed,
            "total_agents": len(results),
            "results": results
        }



multi_agent_scheduler = MultiAgentScheduler()
