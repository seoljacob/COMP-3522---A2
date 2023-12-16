from errors import InvalidDataError
from stuffing import Stuffing
from size import Size
from fabric import Fabric


class StuffedAnimal:
    def __init__(self, **kwargs):
        """
        Initialize a StuffedAnimal object.
        :param kwargs: keyword arguments
        """
        name = kwargs.get("name")
        description = kwargs.get("description")
        sa_id = kwargs.get("product_id")
        self._name = name
        self._description = description
        self._id = sa_id

        InvalidDataError.check_none_or_empty_value(name, "name")
        InvalidDataError.check_none_or_empty_value(description, "description")
        InvalidDataError.check_none_or_empty_value(sa_id, "sa_id")

        stuffing = kwargs.get("stuffing")
        self._stuffing = stuffing

        InvalidDataError.check_none_or_empty_value(stuffing, "stuffing")
        InvalidDataError.check_in_enum(stuffing, Stuffing)

        size = kwargs.get("size")
        self._size = size

        InvalidDataError.check_none_or_empty_value(size, "size")
        InvalidDataError.check_in_enum(size, Size)

        fabric = kwargs.get("fabric")
        self._fabric = fabric

        InvalidDataError.check_none_or_empty_value(fabric, "fabric")
        InvalidDataError.check_in_enum(fabric, Fabric)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def sa_id(self):
        return self._id

    @property
    def stuffing(self):
        return self._stuffing

    @property
    def size(self):
        return self._size

    @property
    def fabric(self):
        return self._fabric

    def __str__(self):
        result = f'{self.name}, {self.description}, {self.sa_id}, {self.stuffing},' \
                 f' {self.size}, {self.fabric}'
        return result
