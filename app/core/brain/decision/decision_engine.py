from app.core.kernel.base_engine import BaseEngine
from app.core.brain.decision.policy_engine import policy_engine


class DecisionEngine(BaseEngine):

    async def decide(self, goal):

        policy = await policy_engine.choose(goal)

        return {
            "goal": goal,
            "mode": policy["mode"],
            "agents": policy["agents"],
            "total_agents": len(policy["agents"]),
            "status": "decision_ready",
        }

    async def run(self, goal):
        return await self.decide(goal)


decision_engine = DecisionEngine()
