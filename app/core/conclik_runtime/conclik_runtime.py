from app.core.conclik_runtime.conclik_executor import conclik_executor


class ConclikRuntime:

    async def run(self, goal):

        return await conclik_executor.execute(goal)


conclik_runtime = ConclikRuntime()
