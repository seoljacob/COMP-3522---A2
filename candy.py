from errors import InvalidDataError


class Candy:
    def __init__(self, **kwargs):
        """
        Initialize a Candy object.
        :param kwargs: keyword arguments
        """
        name = kwargs.get("name")
        description = kwargs.get("description")
        candy_id = kwargs.get("product_id")
        self._name = name
        self._description = description
        self._id = candy_id

        InvalidDataError.check_none_or_empty_value(name, "name")
        InvalidDataError.check_none_or_empty_value(description, "description")
        InvalidDataError.check_none_or_empty_value(candy_id, "candy_id")

        contains_nuts = kwargs.get("has_nuts")
        self._contains_nuts = contains_nuts
        InvalidDataError.check_none_or_empty_value(contains_nuts, "has_nuts")
        InvalidDataError.check_Y_N_value(contains_nuts, "has_nuts")

        is_lactose_free = kwargs.get("has_lactose")
        self._is_lactose_free = is_lactose_free
        InvalidDataError.check_none_or_empty_value(is_lactose_free, "has_lactose")
        InvalidDataError.check_Y_N_value(is_lactose_free, "has_lactose")

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def candy_id(self):
        return self._id

    @property
    def contains_nuts(self):
        return self._contains_nuts

    @property
    def is_lactose_free(self):
        return self._is_lactose_free

    def __str__(self):
        result = f'{self.name}, {self.description}, {self.candy_id}, {self.contains_nuts},' \
                 f' {self.is_lactose_free}'
        return result
