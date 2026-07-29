class NewsProvider:

    def search(self, topic: str):

        return {
            "success": True,
            "provider": "News",

            "topic": topic,

            "articles": [],

            "status": "News Provider Ready",

            "future": [
                "NewsAPI",
                "GNews",
                "Google News RSS",
                "Bing News"
            ]
        }


news_provider = NewsProvider()
