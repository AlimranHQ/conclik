from pathlib import Path


class FileRuntime:

    async def read(self, path: str):

        data = Path(path).read_text()

        return {
            "status": "completed",
            "path": path,
            "content": data,
        }


    async def write(self, path: str, content: str):

        Path(path).write_text(content)

        return {
            "status": "completed",
            "path": path,
        }


file_runtime = FileRuntime()
