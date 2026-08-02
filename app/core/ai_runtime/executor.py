from app.core.master_orchestrator.master_runtime import master_runtime
from app.core.brain.decision.decision_engine import decision_engine
from app.core.brain.assignment.assignment_engine import assignment_engine
from app.core.execution_coordinator.execution_runtime import execution_runtime


class AIExecutor:

    async def execute(self, goal):

        master = await master_runtime.run(goal)

        decision = await decision_engine.decide(goal)

        assignment = await assignment_engine.assign(goal)

        execution = await execution_runtime.run(
            assignment["assignments"]
        )

        return {
            "goal": goal,
            "runtime": "AI Runtime",
            "master": master,
            "decision": decision,
            "assignment": assignment,
            "execution": execution,
        }


ai_executor = AIExecutor()

# Backward Compatibility
ConclikExecutor = AIExecutor
conclik_executor = ai_executor
