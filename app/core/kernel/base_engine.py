class BaseEngine:

    async def run(self, *args, **kwargs):
        raise NotImplementedError

    async def status(self):
        return {
            "status": "ready"
        }

    async def validate(self):
        return True

    async def reset(self):
        return {
            "status": "reset"
        }
