class PlannerExecutor:

    async def execute(self, planner, *args, **kwargs):
        return await planner.run(*args, **kwargs)


planner_executor = PlannerExecutor()
