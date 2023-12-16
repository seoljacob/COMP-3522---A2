from candy import Candy
from pumpkin_caramel_toffee_types import PumpkinCaramelToffeeTypes
from errors import InvalidDataError


class PumpkinCaramelToffee(Candy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_lactose_free = kwargs.get("has_lactose")
        InvalidDataError.check_Y_value(is_lactose_free, "has_lactose")

        contains_nuts = kwargs.get("has_nuts")
        InvalidDataError.check_none_or_empty_value(contains_nuts, "has_nuts")

        toffee_type = kwargs.get("variety")
        self._toffee_type = toffee_type
        InvalidDataError.check_none_or_empty_value(toffee_type, "toffee_type")
        InvalidDataError.check_in_enum(toffee_type, PumpkinCaramelToffeeTypes)

    @property
    def toffee_type(self):
        return self._toffee_type

    def __str__(self):
        result = super().__str__()
        result += f', {self.toffee_type}'
        return result
