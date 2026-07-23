from app.services.research_service import research_service
from app.services.script_service import script_service
from app.services.scene_service import scene_service


class DirectorService:

    def create(
        self,
        topic: str,
        duration: int = 10,
        language: str = "English",
    ):

        research = research_service.generate(topic)

        script = script_service.generate(
            topic=topic,
            duration=duration,
            language=language,
        )

        scenes = scene_service.generate(
            topic=topic,
            duration=duration,
        )

        return {
            "success": True,
            "topic": topic,
            "research": research,
            "script": script,
            "scenes": scenes,
            "status": "Director Ready"
        }


director_service = DirectorService()
