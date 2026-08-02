from app.core.autonomous_runtime.checker.goal_completion_checker import (
    goal_completion_checker,
)
from app.core.autonomous_runtime.replanner.replanner import (
    replanner,
)


class AutonomousRuntime:

    async def run(self, goal, brain_result):

        check = goal_completion_checker.check(brain_result)

        if check["status"] == "goal_completed":
            return {
                "status": "goal_completed",
                "check": check,
            }

        replanned = await replanner.run(goal, check)

        return {
            "status": "continue",
            "check": check,
            "replan": replanned,
        }


autonomous_runtime = AutonomousRuntime()
