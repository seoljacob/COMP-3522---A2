from item_factory import ItemFactory
from rc_spider import RCSpider
from pumpkin_caramel_toffee import PumpkinCaramelToffee
from dancing_skeleton import DancingSkeleton


class HalloweenThemedFactory(ItemFactory):
    """
    HalloweenThemedFactory is responsible for creating Halloween-themed toy, candy, and stuffed animal objects.
    """
    def produce_toy(self, **kwargs) -> RCSpider:
        """
        Create an RC Spider.
        :param kwargs: keyword arguments
        :return: a RCSpider object
        """
        return RCSpider(**kwargs)

    def produce_candy(self, **kwargs) -> PumpkinCaramelToffee:
        """
        Create a Pumpkin Caramel Toffee.
        :param kwargs: keyword arguments
        :return: a PumpkinCaramelToffee
        """
        return PumpkinCaramelToffee(**kwargs)

    def produce_stuffed_animal(self, **kwargs) -> DancingSkeleton:
        """
        Create a Dancing Skeleton.
        :param kwargs: keyword arguments
        :return: a DancingSkeleton object
        """
        return DancingSkeleton(**kwargs)
