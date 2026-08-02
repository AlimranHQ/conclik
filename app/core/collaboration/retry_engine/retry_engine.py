"""
Retry Engine V1
"""

from datetime import datetime, timezone


class RetryEngine:


    def __init__(self, max_retries=3):

        self.max_retries = max_retries

        self.attempts = {}

        self.history = []



    async def register(self, task_id):

        self.attempts[task_id] = 0

        return {
            "task_id": task_id,
            "attempt": 0,
            "status": "registered",
        }



    async def retry(self, task_id, error=None):

        if task_id not in self.attempts:

            await self.register(task_id)


        current = self.attempts[task_id]


        if current >= self.max_retries:

            record = {
                "task_id": task_id,
                "status": "failed",
                "attempt": current,
                "error": error,
                "timestamp": datetime.now(timezone.utc),
            }

            self.history.append(record)

            return record



        current += 1

        self.attempts[task_id] = current


        record = {
            "task_id": task_id,
            "status": "retrying",
            "attempt": current,
            "error": error,
            "timestamp": datetime.now(timezone.utc),
        }


        self.history.append(record)


        return record



    async def get_attempt(self, task_id):

        return self.attempts.get(task_id, 0)



    async def get_history(self):

        return self.history



    async def clear(self):

        self.attempts.clear()

        self.history.clear()


        return {
            "status": "cleared"
        }



retry_engine = RetryEngine()
