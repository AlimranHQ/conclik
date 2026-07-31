class ResultFlowRuntime:

    async def flow(self, previous_output):

        return {
            "input": previous_output,
            "output": previous_output,
            "status": "flowed",
        }


result_flow_runtime = ResultFlowRuntime()
