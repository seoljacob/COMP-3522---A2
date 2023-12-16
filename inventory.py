from errors import InsufficientStockError
from inventory_status import InventoryStatus


class Inventory:
    """
    Inventory class is responsible for stocking the items and providing a status indicator for items.
    """
    def __init__(self):
        # key: item_id(str), value: stock(int)
        self._inventory = {}

    @property
    def inventory(self):
        """
        Returns the inventory.
        :return: a dictionary
        """
        return self._inventory

    def is_initialized(self, product_id: str):
        """
        Checks if the item has been stocked.
        :param product_id: a string representing the product id
        :return: a boolean
        """
        return product_id in self.inventory

    def decrease_stock(self, product_id: str, quantity: int):
        """
        Decreases the stock of the item when it's sold.
        :param product_id: a string representing the product id
        :param quantity: an integer
        """
        curr_quantity = self.inventory[product_id]
        if curr_quantity - quantity < 0:
            raise InsufficientStockError()
        self.inventory[product_id] -= quantity
        print(f"Order has been processed. Now the remaining stock of {product_id} is {self.inventory[product_id]}")

    def print_status_indicator(self, product_id: str):
        """
        Prints the status indicator for the item.
        :param product_id: a string representing the product id
        :return: a string
        """
        stock = self.inventory[product_id]

        if stock >= 10:
            return InventoryStatus.IN_STOCK.value
        elif 3 <= stock < 10:
            return InventoryStatus.LOW.value
        elif 0 < stock < 3:
            return InventoryStatus.VERY_LOW.value
        elif stock == 0:
            return InventoryStatus.OUT_OF_STOCK.value

    def restock(self, product_id: str):
        """
        Increases the stock of the item when it's ordered.
        :param product_id: a string representing the product id
        """
        try:
            self.inventory[product_id] += 100
        except KeyError:
            print(f"The item id {product_id} is initially ordered with 100 item.")
            self.inventory[product_id] = 100

    def display_inventory(self):
        """
        Returns a string representations of the Inventory.
        :return: a string
        """
        if len(self.inventory) == 0:
            print("Inventory is empty.")
        for key, value in self.inventory.items():
            print(f"Item ID {key}: {value}\t{self.print_status_indicator(key)}")
