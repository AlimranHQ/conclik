def youtube_prompt(topic: str):

    return f"""
You are the world's best YouTube SEO Expert.

Topic:
{topic}

Generate:

1. 20 Viral Titles
2. Best SEO Description
3. 50 Hashtags
4. 100 SEO Keywords
5. Thumbnail Text
6. Thumbnail Prompt
7. Best Upload Time
8. Best Country
9. Target Audience
10. Competition Score (/100)
11. Viral Score (/100)
12. Estimated RPM Category
13. Pinned Comment
14. Community Post
15. Shorts Caption
16. Facebook Caption
17. Instagram Caption
18. TikTok Caption

Return everything beautifully formatted.
"""
