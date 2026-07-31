class OrchestratorExecutor:

    async def execute(self, runtime, *args, **kwargs):
        return await runtime.run(*args, **kwargs)


orchestrator_executor = OrchestratorExecutor()
