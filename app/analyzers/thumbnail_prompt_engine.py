class ThumbnailPromptEngine:

    def generate_prompts(self, topic: str, scene_details: str = None):
        # Define styles that usually perform well on social media
        styles = [
            "hyper-realistic 8k",
            "vibrant colors, dramatic lighting",
            "minimalist clean style",
            "3D render, Pixar style"
        ]

        # Base prompt for the main video topic
        main_prompt = (
            f"An eye-catching YouTube thumbnail for a video about '{topic}'. "
            f"Featuring a {styles[1]}, cinematic composition with high contrast. "
            "Focus on facial expressions and bold, legible text placeholder. "
            "Professional, viral style, 16:9 aspect ratio."
        )

        # Specific prompts for individual scenes if details are provided
        scene_prompts = []
        if scene_details:
            scene_prompts.append({
                "for_scene": scene_details[:50] + "...",
                "prompt": (
                    f"Visual prompt for scene: {scene_details}. "
                    "Cinematic shot, 8k resolution, highly detailed, "
                    "suitable for AI image generation like Midjourney."
                )
            })
            # Add another style alternative
            scene_prompts.append({
                 "for_scene": scene_details[:50] + "...",
                 "prompt": (
                    f"Abstract representation of: {scene_details}. "
                    f"Style: {styles[0]}, neon accents, depth of field, "
                    "artstation trend."
                 )
            })

        return {
            "success": True,
            "topic": topic,
            "main_thumbnail_prompt": main_prompt,
            "alternative_scene_prompts": scene_prompts,
            "status": "Thumbnail Prompt Engine Ready"
        }


thumbnail_prompt_engine = ThumbnailPromptEngine()
