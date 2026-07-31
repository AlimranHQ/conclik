from app.core.brain.assignment.assignment_engine import assignment_engine
from app.core.agent_runtime.agent_runtime import agent_runtime


class AssignmentRuntime:

    async def run(self, goal):

        assignment = await assignment_engine.assign(goal)

        results = []

        for item in assignment["assignments"]:

            result = await agent_runtime.execute(
                item["agent"],
                item["task"]
            )

            results.append(result)

        return {
            "status": "assignment_completed",
            "assignment": assignment,
            "results": results,
        }


assignment_runtime = AssignmentRuntime()
