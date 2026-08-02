"""
Autonomous Goal Orchestrator V1
"""

from app.core.autonomous.goal_loop.goal_loop import (
    goal_loop,
)

from app.core.autonomous.control_loop.control_loop import (
    control_loop,
)

from app.core.autonomous.supervisor.supervisor import (
    supervisor,
)



class GoalOrchestrator:


    def __init__(self):

        self.executions = []



    async def execute(
        self,
        goal_id,
        goal
    ):

        created = await goal_loop.create_goal(
            goal_id,
            goal
        )


        await goal_loop.start(
            goal_id
        )


        cycles = await control_loop.start(
            count=1
        )


        supervision = await supervisor.inspect()



        completed = await goal_loop.complete(
            goal_id
        )


        result = {
            "status": "completed",
            "goal_id": goal_id,
            "goal": goal,
            "goal_state": completed,
            "cycles": cycles["cycles"],
            "health": supervision["health"],
        }


        self.executions.append(
            result
        )


        return result



    async def history(self):

        return self.executions



    async def clear(self):

        self.executions.clear()

        await goal_loop.clear()

        await control_loop.clear()

        await supervisor.clear()


        return {
            "status": "cleared"
        }



goal_orchestrator = GoalOrchestrator()
