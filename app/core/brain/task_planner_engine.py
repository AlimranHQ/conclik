from app.core.kernel.base_engine import BaseEngine
from app.core.brain.planner_engine import planner_engine


class TaskPlannerEngine(BaseEngine):

    async def create_graph(self, goal: str):

        plan = await planner_engine.run(goal)

        graph = []

        previous = None

        for index, phase in enumerate(plan["phases"], start=1):

            graph.append({
                "id": index,
                "task": phase,
                "depends_on": [] if previous is None else [previous],
            })

            previous = index

        return {
            "goal": goal,
            "mission": plan["mission"],
            "graph": graph,
            "total_nodes": len(graph),
        }

    async def run(self, goal):
        return await self.create_graph(goal)


task_planner_engine = TaskPlannerEngine()
