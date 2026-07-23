class ImagePromptService:

    def generate(
        self,
        topic: str,
        scene_title: str,
        style: str = "cinematic",
    ):

        prompt = (
            f"{scene_title}, "
            f"{topic}, "
            f"{style}, "
            "ultra realistic, "
            "8k, "
            "masterpiece, "
            "professional lighting, "
            "sharp focus, "
            "high details"
        )

        return {
            "success": True,
            "prompt": prompt,
            "style": style,
            "status": "Image Prompt Ready"
        }


image_prompt_service = ImagePromptService()
