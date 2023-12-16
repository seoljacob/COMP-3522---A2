from candy import Candy
from errors import InvalidDataError


class CremeEggs(Candy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_lactose_free = kwargs.get("has_lactose")
        InvalidDataError.check_Y_value(is_lactose_free, "has_lactose")

        contains_nuts = kwargs.get("has_nuts")
        InvalidDataError.check_none_or_empty_value(contains_nuts, "has_nuts")

        pack_size = kwargs.get("pack_size")
        self._pack_size = pack_size
        InvalidDataError.check_none_or_empty_value(pack_size, "pack_size")
        InvalidDataError.check_non_negative_num(pack_size, "pack_size")

    @property
    def pack_size(self):
        return self._pack_size

    def __str__(self):
        result = super().__str__()
        result += f', {self.pack_size}'
        return result
