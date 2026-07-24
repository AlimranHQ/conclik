from app.core.config import settings
from app.core.logger import logger
from app.core.service_loader import service_loader
from app.core.provider_loader import provider_loader


def get_settings():
    return settings


def get_logger():
    return logger


def get_service_loader():
    return service_loader


def get_provider_loader():
    return provider_loader
