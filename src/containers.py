from dependency_injector import containers, providers

from src.logger import Logger
from src.shipping.services.shipping_service import ShippingService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logger = providers.Singleton(Logger)

    shipping_service = providers.Factory(ShippingService, logger=logger)
