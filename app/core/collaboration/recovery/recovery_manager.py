"""
Recovery Manager V1
"""

from datetime import datetime, timezone


class RecoveryManager:


    def __init__(self):

        self.recovery_points = []

        self.failures = []



    async def create_checkpoint(
        self,
        task_id,
        state,
        metadata=None
    ):

        checkpoint = {
            "task_id": task_id,
            "state": state,
            "metadata": metadata or {},
            "created_at": datetime.now(timezone.utc),
        }

        self.recovery_points.append(
            checkpoint
        )

        return checkpoint



    async def record_failure(
        self,
        task_id,
        error
    ):

        failure = {
            "task_id": task_id,
            "error": error,
            "status": "failed",
            "created_at": datetime.now(timezone.utc),
        }

        self.failures.append(
            failure
        )

        return failure



    async def recover(self, task_id):

        for checkpoint in reversed(
            self.recovery_points
        ):

            if checkpoint["task_id"] == task_id:

                return {
                    "status": "recoverable",
                    "checkpoint": checkpoint,
                }


        return {
            "status": "not_found",
            "task_id": task_id,
        }



    async def get_failures(self):

        return self.failures



    async def clear(self):

        self.recovery_points.clear()

        self.failures.clear()


        return {
            "status": "cleared"
        }



recovery_manager = RecoveryManager()
