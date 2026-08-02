"""
Master Pipeline V1
"""

from app.core.multi_agent.multi_agent_runtime import multi_agent_runtime
from app.core.multi_agent.multi_agent_scheduler import multi_agent_scheduler


class MasterPipeline:

    async def execute(self, goal):

        tasks = [
            "Research",
            "Script",
            "SEO",
            "Thumbnail",
            "Voice",
            "Video",
            "QA",
        ]

        planning = await multi_agent_runtime.run(tasks)

        execution = await multi_agent_scheduler.schedule(
            planning["assignments"],
            goal
        )

        return {
            "status": "pipeline_completed",
            "goal": goal,
            "planning": planning,
            "execution": execution,
        }


master_pipeline = MasterPipeline()
