from app.core.workflow_engine.workflow_executor import workflow_executor


class WorkflowRuntime:

    async def run(self, workflow):

        execution = await workflow_executor.execute(workflow)

        return {
            "status": execution.status,
            "completed": execution.completed,
            "failed": execution.failed,
            "results": execution.results,
            "total_steps": len(execution.results),
        }


workflow_runtime = WorkflowRuntime()
