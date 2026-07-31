from app.core.autonomous_loop.autonomous_cycle import autonomous_cycle


class AutonomousRuntime:

    async def run(self, goal):

        cycle = await autonomous_cycle.execute(goal)

        return {
            "goal": goal,
            "cycle": cycle,
            "steps": len(cycle),
        }


autonomous_runtime = AutonomousRuntime()
