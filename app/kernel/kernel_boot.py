"""
Kernel Boot
"""

from app.kernel.kernel import kernel


async def boot():

    await kernel.start()

