class AutonomousLoop:

    async def run(
        self,
        goal,
        brain_runtime,
        autonomous_runtime,
        max_iterations=3,
    ):

        history = []

        current_goal = goal

        for iteration in range(max_iterations):

            brain = await brain_runtime.run(current_goal)

            auto = await autonomous_runtime.run(
                current_goal,
                brain,
            )

            history.append(auto)

            if auto["status"] == "goal_completed":

                return {
                    "status": "completed",
                    "iterations": iteration + 1,
                    "history": history,
                }

            current_goal = auto["replan"]["goal"]

        return {
            "status": "max_iteration_reached",
            "iterations": max_iterations,
            "history": history,
        }


autonomous_loop = AutonomousLoop()
