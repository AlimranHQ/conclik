from app.core.agent_manager.agent_manager import agent_manager
from app.core.workflow_engine.retry.retry_policy import retry_policy
from app.core.workflow_engine.recovery.failure_recovery import failure_recovery


class WorkflowExecutor:

    async def execute_task(self, task):

        retry_result = await retry_policy.execute(
            lambda: agent_manager.execute(
                task["agent"],
                task["task"]
            ),
            retries=3
        )

        recovery = await failure_recovery.recover(
            task,
            retry_result
        )

        return recovery


workflow_executor = WorkflowExecutor()
