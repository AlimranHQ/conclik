class FailureRecovery:

    async def recover(self, task, result):

        if result["status"] == "completed":
            return {
                "status": "continue",
                "task": task,
                "result": result,
            }

        return {
            "status": "skip",
            "task": task,
            "reason": "retry_failed",
            "result": result,
        }


failure_recovery = FailureRecovery()
