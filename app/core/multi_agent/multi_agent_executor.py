"""
Multi Agent Executor V6
"""

import asyncio

from app.core.multi_agent.multi_agent_router import multi_agent_router


class MultiAgentExecutor:


    async def run_agent(self, item, goal):

        agent_name = item["agent"]

        agent = multi_agent_router.route(
            agent_name
        )

        if agent:

            result = await agent.run(goal)

            return result

        return {
            "status": "agent_not_found",
            "agent": agent_name
        }



    async def execute(self, assignments, goal):

        tasks = []

        for item in assignments:

            tasks.append(
                self.run_agent(
                    item,
                    goal
                )
            )


        results = await asyncio.gather(
            *tasks
        )


        return results



multi_agent_executor = MultiAgentExecutor()
