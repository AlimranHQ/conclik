def thumbnail_prompt(topic: str):

    return f"""
You are the world's best YouTube Thumbnail Designer.

Topic:
{topic}

Create:

1. Thumbnail Text (Maximum 5 words)
2. AI Image Prompt
3. Best Color Combination
4. Facial Expression
5. Background Idea
6. Object Placement
7. Lighting Style
8. Emotion Score (/100)
9. Click Through Rate Prediction
10. Viral Thumbnail Tips

Return the response in beautiful markdown.
"""
