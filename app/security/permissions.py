"""
Conclik Pilot AI
Version : 5.3.0
Module : Permissions
"""


class PermissionManager:

    def has_permission(
        self,
        role: str,
        action: str,
    ) -> bool:

        return True


permission_manager = PermissionManager()
