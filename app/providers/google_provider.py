class GoogleProvider:

    def search(self, query: str):

        return {
            "success": True,
            "provider": "Google Search",

            "query": query,

            "results": [],

            "status": "Google Provider Ready",

            "future": [
                "Google Custom Search API",
                "Serper API",
                "SerpAPI"
            ]
        }


google_provider = GoogleProvider()
