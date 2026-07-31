import asyncio


class RetryPolicy:

    async def execute(
        self,
        executor,
        retries=3
    ):

        last_result = None

        for attempt in range(retries):

            result = await executor()

            last_result = result

            if result.get("status") == "completed":
                return {
                    "status": "completed",
                    "attempt": attempt + 1,
                    "result": result,
                }

            await asyncio.sleep(0.1)

        return {
            "status": "failed",
            "attempt": retries,
            "result": last_result,
        }


retry_policy = RetryPolicy()
