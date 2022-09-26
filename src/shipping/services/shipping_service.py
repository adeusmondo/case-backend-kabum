from decimal import Decimal

from src.config import Config
from src.logger import Logger


class ShippingService:
    def __init__(self, logger: Logger):
        self.logger = logger

    @staticmethod
    def retrieve_shipping_options():
        '''
        This method is used to retrieve the shipping options available for the user
        when database is not available
        '''
        return [
            dict(name='Entrega Ninja',
                 min_height=10,
                 max_height=200,
                 min_width=6,
                 max_width=140,
                 delivery_deadline=6,
                 constant_shipping_calculation=0.3),
            dict(name='Entrega KaBuM',
                 min_height=5,
                 max_height=140,
                 min_width=13,
                 max_width=125,
                 delivery_deadline=4,
                 constant_shipping_calculation=0.2)
        ]

    @staticmethod
    def calculating_shipping_cost(shipping_option, product):
        cost = Decimal((product['weight'] * shipping_option['constant_shipping_calculation']) / 10)
        shipping_option['shipping_cost'] = cost

        return shipping_option

    async def validate_product_dimensions(self, product):
        '''
        This method is used to validate the product dimensions
        '''
        options = []
        product_dimensions = product['dimension']
        shipping_options = self.retrieve_shipping_options()
        self.logger.debug(f'Following shipping options are available: {shipping_options}')

        for shipping_option in shipping_options:
            if (shipping_option['min_height'] <= product_dimensions['height'] <= shipping_option['max_height'] and
                    shipping_option['min_width'] <= product_dimensions['width'] <= shipping_option['max_width']):
                options.append(self.calculating_shipping_cost(shipping_option, product))

        return options

    async def get_shipping_options(self):
        if Config.DB_URL is not None:
            # TODO: Implement this method when database is available
            pass

        return self.retrieve_shipping_options()
