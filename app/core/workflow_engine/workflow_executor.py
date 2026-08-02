from app.core.agent_runtime.agent_runtime import agent_runtime
from app.core.workflow_engine.workflow_result import WorkflowResult


class WorkflowExecutor:

    async def execute(self, workflow):

        result = WorkflowResult()

        for task in workflow.tasks:

            try:
                output = await agent_runtime.execute(
                    task.agent,
                    task.name,
                )

                result.completed.append(task.id)

                result.add_result({
                    "id": task.id,
                    "task": task.name,
                    "agent": task.agent,
                    "status": output.get("status", "completed"),
                    "output": output,
                })

            except Exception as exc:

                result.failed.append(task.id)

                result.add_result({
                    "id": task.id,
                    "task": task.name,
                    "agent": task.agent,
                    "status": "failed",
                    "error": str(exc),
                })

        result.status = (
            "completed"
            if not result.failed
            else "partial_failed"
        )

        return result


workflow_executor = WorkflowExecutor()
