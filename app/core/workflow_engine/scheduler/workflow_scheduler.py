import asyncio

from app.core.workflow_engine.dependency.dependency_resolver import dependency_resolver
from app.core.workflow_engine.executor.workflow_executor import workflow_executor


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

            if parallel:

                parallel_results = await asyncio.gather(
                    *(
                        workflow_executor.execute_task(task)
                        for task in parallel
                    )
                )

                for task, result in zip(parallel, parallel_results):
                    results.append(result)
                    completed.append(task["id"])

            for task in sequential:

                result = await workflow_executor.execute_task(task)

                results.append(result)
                completed.append(task["id"])

        return {
            "status": "scheduler_completed",
            "completed": len(completed),
            "results": results,
        }


workflow_scheduler = WorkflowScheduler()
