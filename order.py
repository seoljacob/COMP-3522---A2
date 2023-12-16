from errors import InvalidDataError
from item_types import ItemTypes
from holiday import Holiday


class Order:
    """
    Order class that represents a single order.
    """
    product_details_key = ['description', 'has_batteries', 'min_age', 'dimensions', 'num_rooms', 'speed', 'jump_height',
                           'has_glow', 'spider_type', 'num_sound', 'colour', 'has_lactose', 'has_nuts', 'variety',
                           'pack_size', 'stuffing', 'size', 'fabric']

    def __init__(self, **kwargs):
        """
        Constructor for Order class.
        :param kwargs: A dictionary of order attributes
        """
        self._order_number = kwargs['order_number']
        self._product_id = kwargs['product_id']
        self._item = kwargs['item']
        self._name = kwargs['name']
        self._quantity = kwargs['quantity']
        self._product_details = self._map_product_details(kwargs)
        self._factory_object = kwargs['item_factory']
        self._errors = []

        self._checkInvalidData()

    def get_order_number(self):

        """
        Returns the order number.
        :return: integer
        """
        return self._order_number

    def set_order_number(self, order_number):
        """
        Sets the order number.
        :param order_number: integer
        :precondition: order_number must be a positive integer
        """
        self._order_number = order_number

    def get_product_id(self):
        """
        Returns the product id.
        :return: string
        """
        return self._product_id

    def set_product_id(self, product_id):
        """
        Sets the product id.
        :param product_id: string
        :precondition: product_id must be a non-null string
        """
        self._product_id = product_id

    def get_item(self):
        """
        Returns the item type.
        :return: string
        """
        return self._item

    def set_item(self, item):
        """
        Sets the item type.
        :param item: string
        :precondition: item must be a valid item type
        """
        self._item = item

    def get_name(self):
        """
        Returns the name of the order.
        :return: string
        """
        return self._name

    def set_name(self, name):
        """
        Sets the name of the order.
        :param name: string
        :precondition: name must be a non-null string
        """
        self._name = name

    def get_quantity(self):
        """
        Returns the quantity of the order.
        :return: integer
        """
        return self._quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the order.
        :param quantity: integer
        :precondition: quantity must be a positive integer
        """
        self._quantity = quantity

    def get_product_details(self):
        """
        Returns the product details.
        :return: dictionary
        """
        return self._product_details

    def set_product_details(self, product_details):
        """
        Sets the product details. 
        :param product_details: dictionary
        :precondition: product_details must be a dictionary with valid keys and values
        """
        self._product_details = product_details

    def get_errors(self):
        """
        Returns the error list.
        :return: list
        """
        return self._errors

    def add_error(self, error):
        """
        Adds an error to the error list.
        :param error: Error
        """
        self._errors.append(error)

    def get_factory_object(self):
        """
        Returns the factory object.
        :return: an ItemFactory
        """
        return self._factory_object

    def set_factory_object(self, factory_object):
        """
        Sets the product details.
        :param factory_object: an ItemFactory
        """
        self._factory_object = factory_object

    order_number = property(get_order_number, set_order_number)
    product_id = property(get_product_id, set_product_id)
    item = property(get_item, set_item)
    name = property(get_name, set_name)
    quantity = property(get_quantity, set_quantity)
    product_details = property(get_product_details, set_product_details)
    errors = property(get_errors)
    factory_object = property(get_factory_object, set_factory_object)

    def __str__(self) -> str:
        """
        Returns a string representation of the Order.
        :return: a string
        """
        if len(self._errors) == 0:
            return f"Order {self.order_number}, Item  {self.item}, Product ID {self.product_id}, " \
                   f"Name \"{self.name}\", Quantity {self.quantity}"
        else:
            formatted_error_msg = ' and '.join([error.get_error_msg() for error in self.errors])
            return f"Order {self.order_number}, Could not process order data was corrupted, " \
                   f"InvalidDataError - {formatted_error_msg}"

    @classmethod
    def _map_product_details(cls, kwargs):
        """Maps the product details to a dictionary.

        :precondition: function must be called
        :postcondition: maps the product details to a dictionary
        :return: a dictionary
        """
        return {key: item for key, item in kwargs.items() if key in cls.product_details_key}

    def _checkInvalidData(self):
        """
        Checks if any invalid data exists.
        """
        # check for order number
        try:
            order_number = int(self.order_number)
            if order_number < 0:
                self.add_error(InvalidDataError("Order number must be a positive integer"))
        except ValueError:
            self.add_error(InvalidDataError("Order number must be a positive integer"))

        # check for product id
        try:
            product_id_striped = self.product_id.strip()
            if not product_id_striped or product_id_striped is None:
                self.add_error(InvalidDataError("Product ID must be a non-null string"))
        except AttributeError:
            self.add_error(InvalidDataError("Product ID must be a non-null string"))

        # check for item
        item_types = [item_type.value for item_type in ItemTypes]
        if self.item not in item_types:
            self.add_error(InvalidDataError(f"Item type must be one of {item_types}"))

        # check for name
        try:
            name_striped = self.name.strip()
            if not name_striped or name_striped is None:
                self.add_error(InvalidDataError("name must be a non-null string"))
        except AttributeError:
            self.add_error(InvalidDataError("name must be a non-null string"))

        # check for quantity
        try:
            if not isinstance(self.quantity, int) or self.quantity < 0:
                self.add_error(InvalidDataError("Quantity must be a positive integer"))
        except ValueError:
            self.add_error(InvalidDataError("Quantity must be a positive integer"))

        # check for factory
        if self.factory_object is None:
            self.add_error(InvalidDataError(f"Holiday must be in {[item.value for item in Holiday]}"))
