from toy import Toy
from errors import InvalidDataError
from robot_bunny_colour import RobotBunnyColour


class RobotBunny(Toy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_operated = kwargs.get("has_batteries")
        min_age = kwargs.get("min_age")

        num_sound = kwargs.get("num_sound")
        self._num_sound = num_sound

        colour = kwargs.get("colour")
        self._colour = colour

        InvalidDataError.check_Y_value(is_operated, "has_batteries")
        InvalidDataError.check_min_age(min_age, 2)

        InvalidDataError.check_none_or_empty_value(num_sound, "num_sound")

        InvalidDataError.check_non_negative_num(num_sound, "num_sound")
        InvalidDataError.check_in_enum(colour, RobotBunnyColour)

    @property
    def num_sound(self):
        return self._num_sound

    @property
    def colour(self):
        return self._colour

    def __str__(self):
        result = super().__str__()
        result += f", {self.num_sound}, {self.colour}"
        return result