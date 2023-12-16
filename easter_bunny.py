from errors import InvalidDataError
from fabric import Fabric
from stuffed_animal import StuffedAnimal
from stuffing import Stuffing
from easter_bunny_colour import EasterBunnyColour


class EasterBunny(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fabric = kwargs.get("fabric")
        InvalidDataError.check_same_value(fabric, Fabric.LINEN.value, "fabric")

        stuffing = kwargs.get("stuffing")
        InvalidDataError.check_same_value(stuffing, Stuffing.POLYESTER_FIBERFILL.value, "stuffing")

        colour = kwargs.get("colour")
        self._colour = colour
        InvalidDataError.check_in_enum(colour, EasterBunnyColour)

    @property
    def colour(self):
        return self._colour

    def __str__(self):
        result = super().__str__()
        result += f", {self.colour}"
        return result
