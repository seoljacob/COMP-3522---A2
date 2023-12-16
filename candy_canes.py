from candy import Candy
from errors import InvalidDataError
from candy_canes_stripe_types import CandyCanesStripeTypes


class CandyCane(Candy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_lactose_free = kwargs.get("has_lactose")
        InvalidDataError.check_N_value(is_lactose_free, "has_lactose")

        contains_nuts = kwargs.get("has_nuts")
        InvalidDataError.check_N_value(contains_nuts, "has_nuts")

        stripe_type = kwargs.get("colour")
        self._stripe_type = stripe_type
        InvalidDataError.check_none_or_empty_value(stripe_type, "stripe_type")
        InvalidDataError.check_in_enum(stripe_type, CandyCanesStripeTypes)

    @property
    def stripe_type(self):
        return self._stripe_type

    def __str__(self):
        result = super().__str__()
        result += f', {self.stripe_type}'
        return result
