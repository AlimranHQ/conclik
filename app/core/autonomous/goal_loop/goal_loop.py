"""
Autonomous Goal Execution Loop V1
"""


from datetime import datetime, timezone



class GoalStatus:

    CREATED = "created"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"



class GoalLoop:


    def __init__(self):

        self.goals = {}

        self.history = []



    async def create_goal(
        self,
        goal_id,
        goal
    ):

        self.goals[goal_id] = {
            "goal": goal,
            "status": GoalStatus.CREATED,
            "progress": 0,
        }


        return self.goals[goal_id]



    async def start(
        self,
        goal_id
    ):

        self.goals[goal_id]["status"] = (
            GoalStatus.RUNNING
        )


        self.history.append(
            {
                "goal_id": goal_id,
                "action": "started",
                "time": datetime.now(timezone.utc),
            }
        )


        return self.goals[goal_id]



    async def progress(
        self,
        goal_id,
        value
    ):

        self.goals[goal_id]["progress"] = value


        self.history.append(
            {
                "goal_id": goal_id,
                "progress": value,
                "time": datetime.now(timezone.utc),
            }
        )


        return self.goals[goal_id]



    async def complete(
        self,
        goal_id
    ):

        self.goals[goal_id]["status"] = (
            GoalStatus.COMPLETED
        )

        self.goals[goal_id]["progress"] = 100


        return self.goals[goal_id]



    async def status(
        self,
        goal_id
    ):

        return self.goals.get(
            goal_id
        )



    async def all_history(
        self
    ):

        return self.history



    async def clear(
        self
    ):

        self.goals.clear()

        self.history.clear()


        return {
            "status": "cleared"
        }



goal_loop = GoalLoop()
