from item_factory import ItemFactory
from robot_bunny import RobotBunny
from creme_eggs import CremeEggs
from easter_bunny import EasterBunny


class EasterThemedFactory(ItemFactory):
    """
    EasterThemedFactory is responsible for creating Easter-themed toy, candy, and stuffed animal objects.
    """

    def produce_toy(self, **kwargs) -> RobotBunny:
        """
        Create a Robot Bunny.
        :param kwargs: keyword arguments
        :return: a RobotBunny object
        """
        return RobotBunny(**kwargs)

    def produce_candy(self, **kwargs) -> CremeEggs:
        """
        Create Crème Eggs.
        :param kwargs: keyword arguments
        :return: a CremeEggs
        """
        return CremeEggs(**kwargs)

    def produce_stuffed_animal(self, **kwargs) -> EasterBunny:
        """
        Create an Easter Bunny.
        :param kwargs: keyword arguments
        :return: a EasterBunny object
        """
        return EasterBunny(**kwargs)
