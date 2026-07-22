from app.prompts.youtube_prompt import youtube_prompt
from app.ai_services import ai_engine


class YouTubeService:

    def generate(self, topic: str):

        prompt = youtube_prompt(topic)

        return ai_engine.generate_content(
            prompt=prompt,
            category="youtube"
        )


youtube_service = YouTubeService()
