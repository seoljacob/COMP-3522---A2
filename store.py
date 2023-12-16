from order import Order
from inventory import Inventory
from errors import InsufficientStockError
from errors import InvalidDataError
from item_types import ItemTypes
from order_database import OrderDatabase

USER_MENU = ['Process Web Orders', 'Check Inventory', 'Exit']


class Store:
    """
    Store class is responsible for receiving orders and maintaining its inventory, getting items from a factory class
    if the store does not have enough stock, and creating the Daily Transaction Report.
    """

    def __init__(self):
        """
        Initialize a Store object.
        """
        self._order_db = OrderDatabase()
        self._inventory = Inventory()

    @property
    def order_db(self):
        """
        Return the Inventory object.
        :return: an Inventory
        """
        return self._order_db

    @property
    def inventory(self):
        """
        Return the Inventory object.
        :return: an Inventory
        """
        return self._inventory

    def download_orders(self, filepath: str):
        """
        Downloads orders from the order Excel file.
        :param filepath: a string representing the file path
        """
        # Read the order file and create orders accordingly
        new_orders = self.order_db.read_order_from_file(filepath)
        self.order_db.add_orders(new_orders)
        return new_orders

    def process_orders(self, orders):
        """
        Processes the received orders.
        """
        # Traverse the downloaded order list
        for order in orders:
            if len(order.errors) == 0:
                # Try to decrease the stocks of each item in the order list
                self.check_item_availability(order)

    def check_item_availability(self, order: Order):
        """
        Checks the item indicated in the order is already on the inventory, if so, decrease the stock, otherwise order
         the item.
        :param order: an Order object
        """
        if self.inventory.is_initialized(order.product_id):
            try:
                self.inventory.decrease_stock(order.product_id, order.quantity)
            except InsufficientStockError:
                self.order_restock_and_decrease_stock(order)
        else:
            self.order_restock_and_decrease_stock(order)

    def order_restock_and_decrease_stock(self, order: Order):
        """
        Order the item through accordingly Item Factory, restock it on the inventory and retry to decrease stock of
        the item.
        :param order: an Order object
        """
        self.order_from_factory(order)
        if len(order.errors) == 0:
            self.inventory.restock(order.product_id)
            self.inventory.decrease_stock(order.product_id, order.quantity)

    @staticmethod
    def order_from_factory(order: Order):
        """
        Order the item through according to the factory object it contains.
        :param order: an Order object
        :return: Toy, StuffedAnimal, Candy
        """
        item = order.item
        details = order.product_details
        details['name'] = order.name
        details['product_id'] = order.product_id
        try:
            if item == ItemTypes.TOY.value:
                order.factory_object.produce_toy(**details)
            elif item == ItemTypes.STUFFED_ANIMAL.value:
                order.factory_object.produce_stuffed_animal(**details)
            elif item == ItemTypes.CANDY.value:
                order.factory_object.produce_candy(**details)
        except InvalidDataError as e:
            order.add_error(e)
            # self.err_order_list[order.order_number] = f"Could not process order data was corrupted, {e}"

    def display_user_menu(self):
        """
        Display the user menu.
        """
        while True:
            print("\n========= GROUP 7 STORE MENU =========")
            for count, menu in enumerate(USER_MENU):
                print(f"{count + 1}, {menu}")
            try:
                user_input = int(input(f"Please enter a number (1 - {len(USER_MENU)}): "))
                if user_input == USER_MENU.index('Process Web Orders') + 1:
                    self.process_web_orders()
                elif user_input == USER_MENU.index('Check Inventory') + 1:
                    self.inventory.display_inventory()
                elif user_input == USER_MENU.index('Exit') + 1:
                    self.order_db.create_daily_transaction_report()
                    print("Thank you.")
                    exit()
                else:
                    raise ValueError(
                        f"Error: Could not process the input. Please enter a number from (1 - {len(USER_MENU)}).")
            except ValueError or TypeError as e:
                print(f"Error: Could not process the input.\n {e}")
            except FileNotFoundError:
                print(f"Error: Could not find the file.")

    def process_web_orders(self):
        """
        Downloads an Excel file of all the online orders placed that day and process them through the system.
        """
        filepath = input("Please input the file path for the online orders: ")
        temp_orders = self.download_orders(filepath)
        self.process_orders(temp_orders)
