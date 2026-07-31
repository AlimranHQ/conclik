from app.core.runtime_tools.terminal_runtime import terminal_runtime
from app.core.runtime_tools.python_runtime import python_runtime
from app.core.runtime_tools.file_runtime import file_runtime


class ToolRouter:

    async def execute(self, tool: str, payload):

        if tool == "terminal":
            return await terminal_runtime.run(payload)

        if tool == "python":
            return await python_runtime.run(payload)

        if tool == "file.read":
            return await file_runtime.read(payload)

        if tool == "file.write":
            return await file_runtime.write(
                payload["path"],
                payload["content"],
            )

        return {
            "status": "unknown_tool",
            "tool": tool,
        }


tool_router = ToolRouter()
