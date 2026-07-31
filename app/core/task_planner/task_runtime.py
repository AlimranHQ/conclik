from app.core.task_planner.task_graph_builder import task_graph_builder


class TaskRuntime:

    async def run(self, tasks):

        graph = await task_graph_builder.build(tasks)

        return {
            "graph": graph,
            "total_nodes": len(graph),
        }


task_runtime = TaskRuntime()
