import time
from order_processor import OrderProcessor


class OrderDatabase:
    """
    OrderDatabase class is responsible for storing the orders and creating the Daily Transaction Report.
    """
    
    def __init__(self):
        """
        Constructor for OrderDatabase class.
        """
        self._orders = []

    def get_orders(self):
        """
        Returns the list of orders.
        """
        return self._orders

    def add_orders(self, new_orders):
        """
        Adds the new orders to the list of orders.
        """
        self._orders = self._orders + new_orders

    orders = property(get_orders)

    def create_daily_transaction_report(self):
        """
        Creates the Daily Transaction Report.
        """
        now = time.localtime()
        filename = "DTR_" + time.strftime("%d%m%Y_%H%M", now) + ".txt"

        try:
            with open(filename, 'a+') as file:
                file.write("GROUP 7 STORE - DAILY TRANSACTION REPORT (DRT)")
                file.write(time.strftime("%d-%m-%Y %H:%M", now))
                file.write('\n')
                for order in self.orders:
                    file.write(f"{order}\n")
            print(f"Daily Transaction Report [{filename}] is successfully created.")
        except Exception as e:
            print(e)

    @staticmethod
    def read_order_from_file(filepath):
        return OrderProcessor.read_order_file(filepath)
