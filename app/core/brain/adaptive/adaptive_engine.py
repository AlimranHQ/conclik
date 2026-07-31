from app.core.kernel.base_engine import BaseEngine


class AdaptiveEngine(BaseEngine):

    async def evolve(self, learning):

        action = learning.get("action", "keep_strategy")

        if action == "keep_strategy":
            mode = "stable"

        elif action == "minor_improvement":
            mode = "adaptive"

        else:
            mode = "evolving"

        return {
            "status": "adaptive_ready",
            "mode": mode,
            "strategy": action,
        }

    async def run(self, learning):
        return await self.evolve(learning)


adaptive_engine = AdaptiveEngine()
