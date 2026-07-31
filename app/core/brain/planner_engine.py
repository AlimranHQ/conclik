from app.core.kernel.base_engine import BaseEngine
from app.core.brain.planner_strategy import planner_strategy


class PlannerEngine(BaseEngine):

    async def create_plan(self, goal: str):

        strategy = await planner_strategy.build(goal)

        return {
            "goal": goal,
            "mission": strategy["mission"],
            "phases": strategy["strategy"],
            "total_phases": len(strategy["strategy"]),
        }

    async def run(self, goal):
        return await self.create_plan(goal)


planner_engine = PlannerEngine()
