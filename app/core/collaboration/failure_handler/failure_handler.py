"""
Failure Handler V1
"""

from datetime import datetime, timezone


class FailureType:

    TRANSIENT = "transient"

    PERMANENT = "permanent"

    UNKNOWN = "unknown"



class FailureSeverity:

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"

    CRITICAL = "critical"



class FailureHandler:


    def __init__(self):

        self.failures = []



    async def capture(
        self,
        task_id,
        error,
        failure_type=FailureType.UNKNOWN,
        severity=FailureSeverity.MEDIUM
    ):

        record = {
            "task_id": task_id,
            "error": str(error),
            "type": failure_type,
            "severity": severity,
            "created_at": datetime.now(timezone.utc),
        }


        self.failures.append(record)


        return record



    async def classify(
        self,
        error
    ):

        message = str(error).lower()


        if (
            "timeout" in message
            or "connection" in message
            or "network" in message
        ):

            return FailureType.TRANSIENT


        if (
            "invalid" in message
            or "permission" in message
        ):

            return FailureType.PERMANENT


        return FailureType.UNKNOWN



    async def should_retry(
        self,
        failure_type
    ):

        return failure_type == FailureType.TRANSIENT



    async def history(self):

        return self.failures



    async def clear(self):

        self.failures.clear()


        return {
            "status": "cleared"
        }



failure_handler = FailureHandler()
