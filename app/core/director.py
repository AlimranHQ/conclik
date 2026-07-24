from app.core.workflow import workflow_engine


class Director:

    def build(self):

        workflow_engine.clear()

        workflow_engine.add_step("Research")

        workflow_engine.add_step("Fact Check")

        workflow_engine.add_step("Script")

        workflow_engine.add_step("Scene")

        workflow_engine.add_step("Image Prompt")

        workflow_engine.add_step("Video Prompt")

        workflow_engine.add_step("Voice")

        workflow_engine.add_step("Subtitle")

        workflow_engine.add_step("SEO")

        workflow_engine.add_step("Thumbnail")

        workflow_engine.add_step("Export")

        return workflow_engine.run()


director = Director()
