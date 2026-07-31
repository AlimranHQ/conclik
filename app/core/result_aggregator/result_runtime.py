from app.core.result_aggregator.result_merger import result_merger


class ResultRuntime:

    async def run(self, executed):

        merged = await result_merger.merge(executed)

        return {
            "summary": merged,
            "total": len(executed),
        }


result_runtime = ResultRuntime()
