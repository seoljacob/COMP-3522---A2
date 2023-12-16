import pandas as pd
from order import Order

from holiday import Holiday
from halloween_themed_factory import HalloweenThemedFactory
from christmas_themed_factory import ChristmasThemedFactory
from easter_themed_factory import EasterThemedFactory


class OrderProcessor:
    """
    OrderProcessor class is responsible for processing orders.
    """

    # Maps holiday types to their respective factories
    holiday_factory_mapper = {
        Holiday.HALLOWEEN.value: HalloweenThemedFactory(),
        Holiday.CHRISTMAS.value: ChristmasThemedFactory(),
        Holiday.EASTER.value: EasterThemedFactory()
    }

    @classmethod
    def read_order_file(cls, filepath):
        """
        Reads the order file and returns a list of Order objects
        :param filepath: The path to the order file
        :return: A list of Order objects
        """
        # df = list(pd.read_excel(filepath).columns)
        orders_dictionary = pd.read_excel(filepath)
        orders_dictionary = orders_dictionary.fillna('')
        orders_dictionary = orders_dictionary.to_dict(orient='records')
        # print(orders_dictionary)
        return cls.create_orders(orders_dictionary)

    @classmethod
    def create_orders(cls, orders_dictionary):
        """
        Creates a list of Order objects from a list of dictionaries.
        :param orders_dictionary: A list of dictionaries
        :return: A list of Order objects
        """
        for order in orders_dictionary:
            order['item_factory'] = cls.holiday_factory_mapper[order['holiday']] \
                if order['holiday'] in cls.holiday_factory_mapper else None

        return [Order(**order) for order in orders_dictionary]

    @classmethod
    def _get_factory(cls, holiday_type):
        """
        Returns the factory reference for the given holiday type.
        :param holiday_type: The holiday type
        :return: The factory reference for the given holiday type
        """
        factory_class = cls.holiday_factory_mapper.get(holiday_type)
        return factory_class
