class SEOAgent:
    async def run(self, goal):
        return {
            "status": "completed",
            "agent": "seo_agent",
            "goal": goal,
            "result": f"SEO completed for: {goal}",
        }

seo_agent = SEOAgent()
