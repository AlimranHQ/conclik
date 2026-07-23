class ServiceLoader:

    def __init__(self):
        self.services = {}

    def register(self, name: str, service):
        self.services[name] = service

    def get(self, name: str):
        return self.services.get(name)

    def all(self):
        return self.services


service_loader = ServiceLoader()
