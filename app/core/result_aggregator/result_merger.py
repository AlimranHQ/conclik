class ResultMerger:

    async def merge(self, results):

        output = []

        for item in results:
            output.append(
                f"[{item['agent']}] {item['task']} -> {item['status']}"
            )

        return "\n".join(output)


result_merger = ResultMerger()
