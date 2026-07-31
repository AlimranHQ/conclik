class DependencyExecutor:

    async def execute(self, graph, *args, **kwargs):
        return await graph.run(*args, **kwargs)


dependency_executor = DependencyExecutor()
