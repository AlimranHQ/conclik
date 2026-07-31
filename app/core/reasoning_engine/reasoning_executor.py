class ReasoningExecutor:

    async def execute(self, engine, *args, **kwargs):
        return await engine.run(*args, **kwargs)


reasoning_executor = ReasoningExecutor()
