"""
Conclik Pilot AI
Application Bootstrap
Version : 1.0.0
"""

from app.bootstrap.provider_bootstrap import initialize_providers


def initialize_application() -> None:
    """
    Initialize the entire Conclik platform.

    Startup Order

    1. Register Providers
    2. Initialize Memory
    3. Initialize Plugins
    4. Initialize Agents
    5. Initialize Workflows
    """

    initialize_providers()

    # Future
    # initialize_memory()
    # initialize_plugins()
    # initialize_agents()
    # initialize_workflows()


if __name__ == "__main__":
    initialize_application()
