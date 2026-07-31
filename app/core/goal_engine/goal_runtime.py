from app.core.goal_engine.goal_decomposer import goal_decomposer


class GoalRuntime:

    async def run(self, goal: str):

        tasks = await goal_decomposer.decompose(goal)

        return {
            "goal": goal,
            "tasks": tasks,
            "total_tasks": len(tasks),
        }


goal_runtime = GoalRuntime()
