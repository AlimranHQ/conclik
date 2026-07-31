from app.core.execution_session.session_runtime import session_runtime

from app.core.brain.goal_engine import goal_engine
from app.core.brain.planner_engine import planner_engine
from app.core.brain.task_planner_engine import task_planner_engine


class MasterRuntime:

    async def run(self, goal):

        session = await session_runtime.create(goal)

        goal_data = await goal_engine.analyze(goal)

        plan = await planner_engine.create_plan(goal)

        graph = await task_planner_engine.create_graph(goal)

        return {
            "status": "accepted",
            "session": session,
            "goal": goal_data,
            "plan": plan,
            "graph": graph,
        }


master_runtime = MasterRuntime()
