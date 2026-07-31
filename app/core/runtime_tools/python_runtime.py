import asyncio


class PythonRuntime:

    async def run(self, code: str):

        process = await asyncio.create_subprocess_exec(
            "python",
            "-c",
            code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await process.communicate()

        return {
            "status": "completed"
            if process.returncode == 0
            else "failed",
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "returncode": process.returncode,
        }


python_runtime = PythonRuntime()
