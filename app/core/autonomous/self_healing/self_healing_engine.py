"""
Autonomous Self Healing Engine V1
"""

from app.core.collaboration.failure_handler.failure_handler import (
    failure_handler,
    FailureType,
)

from app.core.collaboration.retry_engine.retry_engine import (
    retry_engine,
)

from app.core.collaboration.recovery.recovery_manager import (
    recovery_manager,
)


class SelfHealingEngine:


    def __init__(self):

        self.health = "healthy"
        self.history = []



    async def analyze_failure(
        self,
        task_id,
        error
    ):

        failure_type = await failure_handler.classify(
            error
        )


        record = {
            "task_id": task_id,
            "error": str(error),
            "type": failure_type,
        }


        self.history.append(record)


        return record



    async def heal(
        self,
        task_id,
        error
    ):

        analysis = await self.analyze_failure(
            task_id,
            error
        )


        retry_allowed = await failure_handler.should_retry(
            analysis["type"]
        )


        if retry_allowed:

            retry = await retry_engine.retry(
                task_id,
                error
            )

            self.health = "recovering"


            return {
                "status": "retrying",
                "analysis": analysis,
                "retry": retry,
            }



        await recovery_manager.record_failure(
            task_id,
            error
        )


        self.health = "degraded"


        return {
            "status": "recovery_required",
            "analysis": analysis,
        }



    async def status(self):

        return {
            "health": self.health,
            "events": len(self.history),
        }



    async def clear(self):

        self.health = "healthy"

        self.history.clear()


        return {
            "status": "cleared"
        }



self_healing_engine = SelfHealingEngine()
