class DependencyResolver:

    def resolve(self, assignments, completed):

        ready = []
        waiting = []

        completed_ids = set(completed)

        for item in assignments:

            deps = item.get("depends_on", [])

            if all(dep in completed_ids for dep in deps):
                ready.append(item)
            else:
                waiting.append(item)

        return {
            "status": "dependency_ready",
            "ready": ready,
            "waiting": waiting,
        }


dependency_resolver = DependencyResolver()
