class Replanner:

    async def run(self, goal, check_result):

        if check_result["status"] != "replan":
            return {
                "status": "no_replan",
                "goal": goal,
            }

        return {
            "status": "replanned",
            "goal": goal,
            "reason": check_result["reason"],
            "action": "planner_engine",
        }


replanner = Replanner()
