class AutonomousExecutor:

    async def execute(self, core, *args, **kwargs):
        return await core.run(*args, **kwargs)


autonomous_executor = AutonomousExecutor()
