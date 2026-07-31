from app.core.workflow_engine.workflow_executor import workflow_executor


class WorkflowRuntime:

    async def run(self, workflow):

        executed = await workflow_executor.execute(workflow)

        return {
            "workflow": executed,
            "steps": len(executed),
        }


workflow_runtime = WorkflowRuntime()
