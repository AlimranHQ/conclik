from app.core.planner.planner_registry import planner_registry
from app.core.planner.planner_executor import planner_executor


class PlannerGateway:

    async def run(self, planner_name, *args, **kwargs):

        planner = planner_registry.get(planner_name)

        if planner is None:
            raise RuntimeError(
                f"Unknown planner: {planner_name}"
            )

        return await planner_executor.execute(
            planner,
            *args,
            **kwargs,
        )


planner_gateway = PlannerGateway()
