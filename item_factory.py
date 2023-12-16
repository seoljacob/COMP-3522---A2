from abc import ABC, abstractmethod


class ItemFactory(ABC):
    """
    Item Factory class is a base class of Holiday themed factory objects.
    """
    @abstractmethod
    def produce_toy(self, **kwargs):
        """ Abstract method to create a toy. """
        pass

    @abstractmethod
    def produce_stuffed_animal(self, **kwargs):
        """ Abstract method to create a stuffed animal. """
        pass

    @abstractmethod
    def produce_candy(self, **kwargs):
        """ Abstract method to create a candy. """
        pass