"""
Conclik Application Bootstrap
Version : 2.0.0
"""

import asyncio

from app.bootstrap.provider_bootstrap import initialize_providers
from app.kernel.kernel_boot import boot


def initialize_application() -> None:
    """
    Conclik Startup Sequence

    1. Kernel
    2. Providers
    3. Memory
    4. Plugins
    5. Agents
    6. Workflows
    """

    asyncio.run(boot())

    initialize_providers()

    # Future
    # initialize_memory()
    # initialize_plugins()
    # initialize_agents()
    # initialize_workflows()

