import asyncio


class TerminalRuntime:

    async def run(self, command: str):

        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await process.communicate()

        return {
            "status": "completed"
            if process.returncode == 0
            else "failed",

            "command": command,

            "returncode": process.returncode,

            "stdout": stdout.decode(),

            "stderr": stderr.decode(),
        }


terminal_runtime = TerminalRuntime()
