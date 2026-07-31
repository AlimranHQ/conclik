from app.core.kernel.base_engine import BaseEngine


class LearningEngine(BaseEngine):

    async def learn(self, reflection):

        if "reflection" in reflection:
            score = reflection["reflection"].get("score", 0)
        else:
            score = reflection.get("score", 0)

        if score >= 90:
            action = "keep_strategy"
        elif score >= 70:
            action = "minor_improvement"
        else:
            action = "major_improvement"

        return {
            "status": "learning_ready",
            "score": score,
            "action": action,
            "memory_update": True,
        }

    async def run(self, reflection):
        return await self.learn(reflection)


learning_engine = LearningEngine()
