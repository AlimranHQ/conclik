class PolicyEngine:

    async def choose(self, goal):

        text = goal.lower()

        if "youtube" in text:
            return {
                "mode": "content_pipeline",
                "agents": [
                    "research_agent",
                    "script_agent",
                    "seo_agent",
                    "thumbnail_agent",
                    "voice_agent",
                    "video_agent",
                    "qa_agent",
                ],
            }

        if "website" in text:
            return {
                "mode": "software_pipeline",
                "agents": [
                    "research_agent",
                    "planner_agent",
                    "coding_agent",
                    "qa_agent",
                ],
            }

        return {
            "mode": "general_pipeline",
            "agents": [
                "research_agent",
                "planner_agent",
            ],
        }


policy_engine = PolicyEngine()
