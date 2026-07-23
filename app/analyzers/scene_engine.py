class SceneEngine:

    def generate_scenes(self, topic: str, duration: int = 10):
        # Determine number of scenes based on duration (approx. 5 seconds per scene)
        scene_count = max(2, duration // 5)
        
        scenes = []
        
        # Scene 1: The Hook (Critical for retention)
        scenes.append({
            "scene_number": 1,
            "title": "The Hook",
            "duration_seconds": 5,
            "visual_prompt": f"Close up shot introducing the core problem or shocking fact about {topic}.",
            "narration": f"Are you struggling with {topic}? Watch this till the end to discover the secret.",
            "camera_angle": "Eye-level close-up",
            "transition": "Fast zoom-in"
        })

        # Body Scenes
        for i in range(2, scene_count):
            scenes.append({
                "scene_number": i,
                "title": f"Core Point {i-1}",
                "duration_seconds": 5,
                "visual_prompt": f"Dynamic B-roll or animated graphics explaining step {i-1} of {topic}.",
                "narration": f"Step {i-1}: Breaking down the essential details and practical applications.",
                "camera_angle": "Medium shot with smooth panning",
                "transition": "Clean cut"
            })

        # Final Scene: Call to Action (CTA)
        scenes.append({
            "scene_number": scene_count,
            "title": "Call to Action (CTA)",
            "duration_seconds": 5,
            "visual_prompt": f"Engaging outro screen with subscribe button and related topic preview for {topic}.",
            "narration": "If you found this helpful, hit subscribe and let us know your thoughts in the comments!",
            "camera_angle": "Wide angle shot",
            "transition": "Fade to black"
        })

        return {
            "success": True,
            "topic": topic,
            "total_scenes": len(scenes),
            "estimated_duration": duration,
            "scenes": scenes,
            "status": "Scene Engine Ready"
        }


scene_engine = SceneEngine()
