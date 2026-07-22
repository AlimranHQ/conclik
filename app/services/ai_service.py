from app.ai_services import ai_engine


class AIService:

    def generate(
        self,
        prompt: str,
        category: str = "general",
        provider: str = "auto"
    ):
        return ai_engine.generate_content(
            prompt=prompt,
            category=category,
            provider=provider
        )


ai_service = AIService()
