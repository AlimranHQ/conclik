from app.core.agents.base_agent import BaseAgent
from app.core.collaboration.event_bus.subscriber import subscriber
from app.core.collaboration.event_bus.publisher import publisher


class ScriptAgent(BaseAgent):

    @property
    def name(self):
        return "script_agent"

    async def run(self, goal):

        event = await subscriber.receive()

        research = None

        if event:
            research = event.payload

        result = {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "research": research,
            "result": f"Script completed for: {goal}",
        }

        await publisher.publish(
            "script_completed",
            self.name,
            result,
        )

        return result


script_agent = ScriptAgent()
