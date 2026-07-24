"""
Conclik Pilot AI
Version : 4.8.1
Module : Model Selector
"""


class ModelSelector:

    def gemini(self):
        return "models/gemini-3.5-flash"

    def fallback(self):
        return "models/gemini-2.0-flash"


model_selector = ModelSelector()
