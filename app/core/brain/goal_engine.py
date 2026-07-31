from app.core.kernel.base_engine import BaseEngine


class GoalEngine(BaseEngine):

    async def analyze(self, goal: str):

        goal = goal.strip()

        return {
            "goal": goal,
            "category": "general",
            "priority": "high",
            "status": "accepted",
        }

    async def run(self, goal):
        return await self.analyze(goal)


goal_engine = GoalEngine()
