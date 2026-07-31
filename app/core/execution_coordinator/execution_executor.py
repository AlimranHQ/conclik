class ExecutionExecutor:

    async def execute(self, assignments):

        results = []

        for item in assignments:

            results.append(
                {
                    "task": item["task"],
                    "agent": item["agent"],
                    "status": "completed",
                }
            )

        return results


execution_executor = ExecutionExecutor()
