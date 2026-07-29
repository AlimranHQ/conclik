class WikipediaProvider:

    def search(self, topic: str):

        return {
            "success": True,
            "provider": "Wikipedia",

            "topic": topic,

            "summary": "",

            "references": [],

            "status": "Wikipedia Provider Ready",

            "future": [
                "Wikipedia API",
                "Wikidata",
                "Wikimedia Commons"
            ]
        }


wikipedia_provider = WikipediaProvider()
