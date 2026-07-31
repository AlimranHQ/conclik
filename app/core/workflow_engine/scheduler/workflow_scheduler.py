import asyncio

from app.core.parallel_executor.parallel_executor import parallel_executor
from app.core.agent_manager.agent_manager import agent_manager
from app.core.workflow_engine.dependency.dependency_resolver import dependency_resolver


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

                execution = await parallel_executor.execute(
                    parallel
                )

                for r, task in zip(execution["results"], parallel):
                    results.append(r)
                    completed.append(task["id"])

            for task in sequential:

                r = await agent_manager.execute(
                    task["agent"],
                    task["task"]
                )

                results.append(r)
                completed.append(task["id"])

        return {
            "status": "scheduler_completed",
            "completed": len(completed),
            "results": results,
        }


workflow_scheduler = WorkflowScheduler()
