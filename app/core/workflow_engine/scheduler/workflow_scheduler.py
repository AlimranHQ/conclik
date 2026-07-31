import asyncio

from app.core.parallel_executor.parallel_executor import parallel_executor
from app.core.agent_manager.agent_manager import agent_manager
from app.core.workflow_engine.dependency.dependency_resolver import dependency_resolver
from app.core.workflow_engine.retry.retry_policy import retry_policy


class WorkflowScheduler:

    async def execute(self, assignments):

        completed = []
        results = []

        while True:

            state = dependency_resolver.resolve(
                assignments,
                completed
            )

            ready = [
                item for item in state["ready"]
                if item["id"] not in completed
            ]

            if not ready:
                break

            parallel = [
                item for item in ready
                if not item["depends_on"]
            ]

            sequential = [
                item for item in ready
                if item["depends_on"]
            ]

            #
            # Parallel Tasks
            #
            if parallel:

                async def run_parallel(task):

                    return await retry_policy.execute(
                        lambda: agent_manager.execute(
                            task["agent"],
                            task["task"]
                        ),
                        retries=3,
                    )

                parallel_results = await asyncio.gather(
                    *(run_parallel(task) for task in parallel)
                )

                for task, result in zip(parallel, parallel_results):
                    results.append(result)
                    completed.append(task["id"])

            #
            # Sequential Tasks
            #
            for task in sequential:

                result = await retry_policy.execute(
                    lambda: agent_manager.execute(
                        task["agent"],
                        task["task"]
                    ),
                    retries=3,
                )

                results.append(result)
                completed.append(task["id"])

        return {
            "status": "scheduler_completed",
            "completed": len(completed),
            "results": results,
        }


workflow_scheduler = WorkflowScheduler()
