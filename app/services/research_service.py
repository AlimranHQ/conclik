from app.providers.google_provider import google_provider
from app.providers.wikipedia_provider import wikipedia_provider
from app.providers.news_provider import news_provider

from app.services.fact_checker import fact_checker
from app.services.knowledge_engine import knowledge_engine


class ResearchService:

    def research(
        self,
        topic: str,
        language: str = "English",
    ):

        google = google_provider.search(topic)

        wikipedia = wikipedia_provider.search(topic)

        news = news_provider.search(topic)

        verified = fact_checker.verify(
            {
                "google": google,
                "wikipedia": wikipedia,
                "news": news,
            }
        )

        knowledge = knowledge_engine.merge(
            google=google,
            wikipedia=wikipedia,
            news=news,
        )

        return {
            "success": True,
            "topic": topic,
            "language": language,
            "research": knowledge,
            "fact_check": verified,
            "status": "Research Pipeline Ready"
        }


research_service = ResearchService()
