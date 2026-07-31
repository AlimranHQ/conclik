from app.core.dependency_graph.dependency_registry import dependency_registry
from app.core.dependency_graph.dependency_executor import dependency_executor


class DependencyRuntime:

    async def run(self, graph_name, *args, **kwargs):

        graph = dependency_registry.get(graph_name)

        if graph is None:
            raise RuntimeError(
                f"Unknown dependency graph: {graph_name}"
            )

        return await dependency_executor.execute(
            graph,
            *args,
            **kwargs,
        )


dependency_runtime = DependencyRuntime()
