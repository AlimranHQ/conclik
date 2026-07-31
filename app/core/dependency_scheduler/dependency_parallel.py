class DependencyParallel:

    async def group(self, tasks):

        if len(tasks) < 5:
            return [tasks]

        return [
            ["Research"],
            ["Planning"],
            ["Script"],
            ["SEO", "Thumbnail", "Voice"],
            ["Video"],
            ["QA"],
            ["Publish"],
        ]


dependency_parallel = DependencyParallel()
