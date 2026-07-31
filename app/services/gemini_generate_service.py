from app.core.intelligence.intelligence_engine import intelligence_engine


class GeminiGenerateService:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
    ):

        return await intelligence_engine.generate(
            prompt=prompt,
            category=category,
            preferred_provider="gemini",
        )


gemini_generate_service = GeminiGenerateService()
