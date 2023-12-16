from stuffed_animal import StuffedAnimal
from errors import InvalidDataError
from fabric import Fabric
from stuffing import Stuffing


class DancingSkeleton(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fabric = kwargs.get("fabric")
        InvalidDataError.check_same_value(fabric, Fabric.ACRYLIC.value, "fabric")

        stuffing = kwargs.get("stuffing")
        InvalidDataError.check_same_value(stuffing, Stuffing.POLYESTER_FIBERFILL.value, "stuffing")

        has_glow = kwargs.get("has_glow")
        self._has_glow = has_glow
        InvalidDataError.check_none_or_empty_value(has_glow, "has_glow")
        InvalidDataError.check_Y_value(has_glow, "has_glow")

    @property
    def has_glow(self):
        return self._has_glow

    def __str__(self):
        result = super().__str__()
        result += f", {self.has_glow}"
        return result
