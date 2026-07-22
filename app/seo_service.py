from app.ai_services import ai_engine
from app.prompts.seo_prompt import YOUTUBE_SEO_PROMPT


class SEOService:

    def generate(
        self,
        topic: str,
        language: str = "English"
    ):

        prompt = YOUTUBE_SEO_PROMPT.format(
            topic=topic,
            language=language
        )

        return ai_engine.generate_content(
            prompt=prompt,
            category="seo"
        )


seo_service = SEOService()
