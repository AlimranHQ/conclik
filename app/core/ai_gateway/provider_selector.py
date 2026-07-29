class ProviderSelector:

    def select(self, provider=None):
        return provider or "gemini"

provider_selector = ProviderSelector()
