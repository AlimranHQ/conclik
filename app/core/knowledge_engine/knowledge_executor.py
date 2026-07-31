class KnowledgeExecutor:

    async def execute(self, engine, *args, **kwargs):
        return await engine.run(*args, **kwargs)


knowledge_executor = KnowledgeExecutor()
