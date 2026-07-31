from app.core.self_improvement.self_learning import self_learning


class SelfRuntime:

    async def run(self, reflection):

        return await self_learning.improve(reflection)


self_runtime = SelfRuntime()
