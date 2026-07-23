class ProviderLoader:

    def __init__(self):
        self.providers = {}

    def register(self, name: str, provider):
        self.providers[name] = provider

    def get(self, name: str):
        return self.providers.get(name)

    def available(self):
        return list(self.providers.keys())


provider_loader = ProviderLoader()
