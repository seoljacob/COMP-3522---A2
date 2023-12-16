from enum import Enum


class InventoryStatus(Enum):
    """
    Inventory status.
    """
    LOW = "low"
    VERY_LOW = "very low"
    IN_STOCK = "in stock"
    OUT_OF_STOCK = "out of stock"
