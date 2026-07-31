from app.core.dependency_scheduler.dependency_parallel import dependency_parallel


class DependencyRuntime:

    async def run(self, tasks):

        groups = await dependency_parallel.group(tasks)

        return {
            "parallel_groups": groups,
            "groups": len(groups),
        }


dependency_runtime = DependencyRuntime()
