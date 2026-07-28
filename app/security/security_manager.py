"""
Conclik Pilot AI
Version : 5.4.0
Module : Security Manager
"""

from app.security.validator import request_validator
from app.security.auth import authentication
from app.security.permissions import permission_manager
from app.security.audit import audit_logger
from app.security.rate_limiter import rate_limiter


class SecurityManager:

    def validate(self, prompt: str) -> bool:
        return request_validator.validate(prompt)

    def authenticate(self) -> bool:
        return authentication.authenticate()

    def authorize(self, role: str = "user", action: str = "general") -> bool:
        return permission_manager.has_permission(role, action)

    def allow(self, identifier: str = "anonymous") -> bool:
        return rate_limiter.allow(identifier)

    def audit(self, event: str, source: str = "system"):
        return audit_logger.log(event, source)

    def secure(
        self,
        prompt: str,
        role: str = "user",
        action: str = "general",
        identifier: str = "anonymous",
    ) -> bool:

        if not self.validate(prompt):
            return False

        if not self.authenticate():
            return False

        if not self.authorize(role, action):
            return False

        if not self.allow(identifier):
            return False

        self.audit("Security Check Passed", source="SecurityManager")

        return True


security_manager = SecurityManager()
