"""
Kernel Shutdown
"""

from app.kernel.kernel import kernel


async def shutdown():

    await kernel.shutdown()

