import asyncio

from app.core.agent_manager.agent_manager import agent_manager


class ParallelExecutor:

    async def execute(self, assignments):

        tasks = []

        for item in assignments:

            tasks.append(

                agent_manager.execute(
                    item["agent"],
                    item["task"]
                )

            )

        results = await asyncio.gather(*tasks)

        return {
            "status": "parallel_completed",
            "completed": len(results),
            "results": results,
        }


parallel_executor = ParallelExecutor()
