from item_factory import ItemFactory
from santas_workshop import SantasWorkshop
from candy_canes import CandyCane
from reindeer import Reindeer


class ChristmasThemedFactory(ItemFactory):
    """
    ChristmasThemedFactory is responsible for creating Christmas-themed toy, candy, and stuffed animal objects.
    """
    def produce_toy(self, **kwargs) -> SantasWorkshop:
        """
        Create a Santa's Workshop.
        :param kwargs: keyword arguments
        :return: a SantasWorkshop object
        """
        return SantasWorkshop(**kwargs)

    def produce_candy(self, **kwargs) -> CandyCane:
        """
        Create a Candy Cane.
        :param kwargs: keyword arguments
        :return: a CandyCane object
        """
        return CandyCane(**kwargs)

    def produce_stuffed_animal(self, **kwargs) -> Reindeer:
        """
        Create a Reindeer.
        :param kwargs: keyword arguments
        :return: a Reindeer object
        """
        return Reindeer(**kwargs)
