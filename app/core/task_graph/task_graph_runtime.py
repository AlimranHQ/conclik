from app.core.task_graph.task_graph_registry import task_graph_registry
from app.core.task_graph.task_graph_executor import task_graph_executor


class TaskGraphRuntime:

    async def run(self, graph_name, *args, **kwargs):

        graph = task_graph_registry.get(graph_name)

        if graph is None:
            raise RuntimeError(
                f"Unknown task graph: {graph_name}"
            )

        return await task_graph_executor.execute(
            graph,
            *args,
            **kwargs,
        )


task_graph_runtime = TaskGraphRuntime()
