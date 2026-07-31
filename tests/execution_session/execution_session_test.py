import asyncio

from app.core.execution_session.session_runtime import session_runtime

print("=== Execution Session Test ===")


async def main():

    session = await session_runtime.create(
        "Build Conclik AI OS"
    )

    print(session)

    assert session["status"] == "running"
    assert session["goal"] == "Build Conclik AI OS"

    print("PASS | Execution Session working")


asyncio.run(main())
