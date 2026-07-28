"""
Conclik Pilot AI
Version : 5.3.0
Module : Audit Logger
"""


class AuditLogger:

    def log(
        self,
        event: str,
        source: str = "system",
    ):

        print(f"[AUDIT] {source}: {event}")

        return True


audit_logger = AuditLogger()
