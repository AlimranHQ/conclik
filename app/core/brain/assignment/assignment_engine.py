from app.core.kernel.base_engine import BaseEngine
from app.core.brain.assignment.assignment_policy import assignment_policy
from app.core.brain.task_planner_engine import task_planner_engine


class AssignmentEngine(BaseEngine):

    async def assign(self, goal):

        plan = await task_planner_engine.run(goal)

        assignments = await assignment_policy.build(plan)

        return {
            "goal": goal,
            "assignments": assignments,
            "total_assignments": len(assignments),
            "status": "assignment_ready",
        }

    async def run(self, goal):
        return await self.assign(goal)


assignment_engine = AssignmentEngine()
