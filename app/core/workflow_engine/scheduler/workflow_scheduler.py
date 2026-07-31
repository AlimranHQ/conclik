import asyncio

from app.core.parallel_executor.parallel_executor import parallel_executor
from app.core.agent_manager.agent_manager import agent_manager


class WorkflowScheduler:

    async def execute(self, workflow):

        results = []

        # Execute all parallel tasks together
        if workflow["parallel"]:
            parallel_result = await parallel_executor.execute(
                workflow["parallel"]
            )
            results.extend(parallel_result["results"])

        # Execute dependent tasks one by one
        for item in workflow["sequential"]:
            result = await agent_manager.execute(
                item["agent"],
                item["task"]
            )
            results.append(result)

        return {
            "status": "scheduler_completed",
            "completed": len(results),
            "results": results,
        }


workflow_scheduler = WorkflowScheduler()
