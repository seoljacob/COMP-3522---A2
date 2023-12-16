from toy import Toy
from errors import InvalidDataError


class SantasWorkshop(Toy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_operated = kwargs.get("has_batteries")
        dimensions = kwargs.get("dimensions")
        self._dimensions = dimensions

        num_rooms = kwargs.get("num_rooms")
        self._num_rooms = num_rooms

        InvalidDataError.check_N_value(is_operated, "has_batteries")

        InvalidDataError.check_none_or_empty_value(dimensions, "dimensions")
        InvalidDataError.check_negative_dimensions(dimensions, "dimensions")

        InvalidDataError.check_none_or_empty_value(num_rooms, "num_rooms")
        InvalidDataError.check_non_negative_num(num_rooms, "num_rooms")

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def num_rooms(self):
        return self._num_rooms

    def __str__(self):
        result = super().__str__()
        result += f', {self.dimensions}, {self.num_rooms}'
        return result
