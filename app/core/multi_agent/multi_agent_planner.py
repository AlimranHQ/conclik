class MultiAgentPlanner:

    async def assign(self, tasks):

        mapping = {
            "Research": "research_agent",
            "Planning": "research_agent",
            "Script": "script_agent",
            "SEO": "seo_agent",
            "Thumbnail": "thumbnail_agent",
            "Voice": "voice_agent",
            "Video": "video_agent",
            "QA": "qa_agent",
            "Publish": "qa_agent",
        }

        return [
            {
                "task": task,
                "agent": mapping.get(task, "research_agent"),
            }
            for task in tasks
        ]


multi_agent_planner = MultiAgentPlanner()
