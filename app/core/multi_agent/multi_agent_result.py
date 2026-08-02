"""
Multi Agent Result V5
"""


class MultiAgentResult:

    def __init__(self):

        self.status = "pending"

        self.results = []

        self.success = []

        self.failed = []


    def add(self, result):

        self.results.append(result)

        if result.get("status") == "completed":

            self.success.append(
                result.get("agent")
            )

        else:

            self.failed.append(
                result.get("agent")
            )


    def finalize(self):

        self.status = "completed"


multi_agent_result = MultiAgentResult()
