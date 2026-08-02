"""
Master Monitor V1
"""


class MasterMonitor:

    def __init__(self):

        self.metrics = {
            "runs": 0,
            "success": 0,
            "failed": 0,
        }


    def record_success(self):

        self.metrics["runs"] += 1
        self.metrics["success"] += 1


    def record_failure(self):

        self.metrics["runs"] += 1
        self.metrics["failed"] += 1


    def report(self):

        return self.metrics


master_monitor = MasterMonitor()
