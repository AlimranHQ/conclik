from app.core.agent_runtime.agent_runtime import agent_runtime


class AgentPipeline:

    async def run(self, goal):

        stages = [
            "research_agent",
            "script_agent",
            "seo_agent",
            "thumbnail_agent",
            "voice_agent",
            "video_agent",
            "qa_agent",
        ]

        results = []

        for agent in stages:

            result = await agent_runtime.execute(
                agent,
                goal,
            )

            results.append(result)

        return {
            "status": "pipeline_completed",
            "total_agents": len(stages),
            "results": results,
        }


agent_pipeline = AgentPipeline()
