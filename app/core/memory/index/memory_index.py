class MemoryIndex:

    def __init__(self):
        self.index = {}

    def add(self, goal, record):
        self.index[goal.lower()] = record

    def search(self, query):

        query = query.lower()

        results = {}

        for goal, record in self.index.items():

            if query in goal:
                results[goal] = record

        return {
            "status": "memory_found",
            "results": results,
            "count": len(results),
        }


memory_index = MemoryIndex()
