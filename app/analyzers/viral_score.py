class ViralScoreAnalyzer:

    def analyze(
        self,
        title: str,
        description: str,
        hashtags: list[str] = None,
    ):
        if hashtags is None:
            hashtags = []

        recommendations = []

        # 1. Title Score Logic (Ideal length: 40-70 characters)
        title_length = len(title)
        if 40 <= title_length <= 70:
            title_score = 95
        elif title_length < 40:
            title_score = 70
            recommendations.append("Make your title longer (aim for 40-70 characters) for better reach.")
        else:
            title_score = 75
            recommendations.append("Title is a bit too long. Keep it concise (under 70 characters).")

        # Check for Power/Curiosity Words in Title
        power_words = ["secret", "ultimate", "best", "how to", "why", "proven", "powerful", "amazing"]
        has_power_word = any(word in title.lower() for word in power_words)
        if has_power_word:
            title_score = min(100, title_score + 5)
        else:
            recommendations.append("Add curiosity or power words (e.g., 'Ultimate', 'Secret', 'How to') to the title.")

        # 2. Description Score Logic (Ideal length: 200+ characters)
        desc_length = len(description)
        if desc_length >= 200:
            description_score = 90
        elif desc_length >= 100:
            description_score = 75
            recommendations.append("Expand your description (aim for 200+ characters) with more context.")
        else:
            description_score = 50
            recommendations.append("Description is too short. Add a detailed summary and timestamps.")

        # 3. Hashtag Score Logic (Ideal count: 3 to 5 tags)
        tag_count = len(hashtags)
        if 3 <= tag_count <= 5:
            hashtag_score = 95
        elif tag_count > 5:
            hashtag_score = 70
            recommendations.append("Too many hashtags. Stick to 3-5 highly relevant tags.")
        else:
            hashtag_score = 60
            recommendations.append("Add at least 3-5 relevant hashtags to improve discoverability.")

        # 4. Other placeholders (Hook & Thumbnail can be integrated later)
        thumbnail_score = 80 if title_length > 0 else 0
        hook_score = 85 if has_power_word else 65

        if not has_power_word:
            recommendations.append("Improve Hook: Grab the viewer's attention within the first 3 seconds.")

        # Calculate Overall Viral Score (Weighted Average)
        overall_score = int(
            (title_score * 0.3) +
            (description_score * 0.2) +
            (hashtag_score * 0.1) +
            (thumbnail_score * 0.2) +
            (hook_score * 0.2)
        )

        # Default fallback recommendations if everything looks great
        if not recommendations:
            recommendations.append("Great job! Your metadata looks optimized for high engagement.")

        return {
            "success": True,
            "title_score": title_score,
            "description_score": description_score,
            "hashtag_score": hashtag_score,
            "thumbnail_score": thumbnail_score,
            "hook_score": hook_score,
            "seo_score": int((title_score + description_score + hashtag_score) / 3),
            "viral_score": overall_score,
            "recommendation": recommendations,
            "status": "Viral Analyzer Dynamic Engine Ready"
        }


viral_score = ViralScoreAnalyzer()
