class TaskGraphExecutor:

    async def execute(self, graph, *args, **kwargs):
        return await graph.run(*args, **kwargs)


task_graph_executor = TaskGraphExecutor()
