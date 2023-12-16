from errors import InvalidDataError


class Toy:
    def __init__(self, **kwargs):
        """
        Initialize a Toy object.
        :param kwargs: keyword arguments
        """
        name = kwargs.get("name")
        description = kwargs.get("description")
        toy_id = kwargs.get("product_id")
        self._name = name
        self._description = description
        self._id = toy_id

        InvalidDataError.check_none_or_empty_value(name, "name")
        InvalidDataError.check_none_or_empty_value(description, "description")
        InvalidDataError.check_none_or_empty_value(toy_id, "toy_id")

        is_operated = kwargs.get("has_batteries")
        self._is_operated = is_operated

        min_age = kwargs.get("min_age")
        self._min_age = min_age

        InvalidDataError.check_none_or_empty_value(is_operated, "has_operated")
        InvalidDataError.check_Y_N_value(is_operated, "has_operated")

        InvalidDataError.check_none_or_empty_value(min_age, "min_age")
        InvalidDataError.check_non_negative_num(min_age, "min_age")

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def toy_id(self):
        return self._id

    @property
    def is_operated(self):
        return self._is_operated

    @property
    def min_age(self):
        return self._min_age

    def __str__(self):
        result = f'{self.name}, {self.description}, {self.toy_id}, {self.is_operated}, {self.min_age}'
        return result
