from app.core.agent_registry.agent_registry import list_agents


class AgentSelector:

    def select(self, task):

        task = task.lower()

        mapping = {
            "research": "research_agent",
            "planning": "research_agent",
            "script": "script_agent",
            "seo": "seo_agent",
            "thumbnail": "thumbnail_agent",
            "voice": "voice_agent",
            "video": "video_agent",
            "quality": "qa_agent",
            "qa": "qa_agent",
            "publish": "qa_agent",
            "optimization": "seo_agent",
        }

        for key, agent in mapping.items():
            if key in task:
                return agent

        return "research_agent"

    def available(self):
        return list_agents()


agent_selector = AgentSelector()
