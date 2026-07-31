class TaskGraphBuilder:

    async def build(self, tasks):

        graph = []

        for index, task in enumerate(tasks):

            graph.append(
                {
                    "id": index + 1,
                    "task": task,
                    "depends_on": [] if index == 0 else [index],
                }
            )

        return graph


task_graph_builder = TaskGraphBuilder()
