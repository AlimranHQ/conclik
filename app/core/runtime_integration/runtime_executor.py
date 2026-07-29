class RuntimeExecutor:

    async def execute(self, runtime, *args, **kwargs):
        return await runtime.run(*args, **kwargs)


runtime_executor = RuntimeExecutor()
