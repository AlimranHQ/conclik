"""
Master Reliability Layer V1
"""

from app.core.collaboration.failure_handler.failure_handler import (
    failure_handler,
    FailureType,
)

from app.core.collaboration.retry_engine.retry_engine import (
    retry_engine,
)

from app.core.collaboration.recovery.recovery_manager import (
    recovery_manager,
)



class MasterReliability:


    def __init__(self):

        self.active_tasks = {}



    async def start_task(self, task_id):

        self.active_tasks[task_id] = {
            "status": "running"
        }

        await recovery_manager.create_checkpoint(
            task_id,
            "running",
            {
                "source": "master_orchestrator"
            }
        )

        return {
            "task_id": task_id,
            "status": "started"
        }



    async def handle_failure(
        self,
        task_id,
        error
    ):

        failure_type = await failure_handler.classify(
            error
        )


        await failure_handler.capture(
            task_id,
            error,
            failure_type,
        )


        retry_allowed = await failure_handler.should_retry(
            failure_type
        )


        if retry_allowed:

            retry = await retry_engine.retry(
                task_id,
                error
            )

            return {
                "status": "retrying",
                "retry": retry,
            }


        await recovery_manager.record_failure(
            task_id,
            error
        )


        return {
            "status": "failed",
            "recovery": "required",
        }



    async def recover_task(
        self,
        task_id
    ):

        return await recovery_manager.recover(
            task_id
        )



    async def clear(self):

        self.active_tasks.clear()

        await failure_handler.clear()

        await retry_engine.clear()

        await recovery_manager.clear()


        return {
            "status": "cleared"
        }



master_reliability = MasterReliability()
