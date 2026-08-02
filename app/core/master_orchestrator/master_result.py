"""
Master Result V1
"""


class MasterResult:

    def __init__(self):

        self.status = "pending"
        self.results = []
        self.errors = []


    def add_result(self, result):

        self.results.append(result)


    def add_error(self, error):

        self.errors.append(error)


    def complete(self):

        self.status = "completed"


    def fail(self):

        self.status = "failed"


    def output(self):

        return {
            "status": self.status,
            "results": self.results,
            "errors": self.errors,
            "total": len(self.results),
        }


master_result = MasterResult()
