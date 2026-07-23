class KnowledgeEngine:

    def merge(
        self,
        google=None,
        wikipedia=None,
        news=None,
    ):

        return {
            "success": True,

            "knowledge": {

                "google": google,

                "wikipedia": wikipedia,

                "news": news,
            },

            "status": "Knowledge Engine Ready"
        }


knowledge_engine = KnowledgeEngine()
