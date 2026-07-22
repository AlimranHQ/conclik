from app.prompts.thumbnail_prompt import thumbnail_prompt
from app.ai_services import ai_engine


class ThumbnailService:

    def generate(self, topic: str):

        prompt = thumbnail_prompt(topic)

        result = ai_engine.generate_content(
            prompt=prompt,
            category="thumbnail",
        )

        return result


thumbnail_service = ThumbnailService()
