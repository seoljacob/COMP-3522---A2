from toy import Toy
from errors import InvalidDataError
from spider_types import SpiderTypes


class RCSpider(Toy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        is_operated = kwargs.get("has_batteries")

        speed = kwargs.get("speed")
        self._speed = speed

        jump_height = kwargs.get("jump_height")
        self._jump_height = jump_height

        has_glow = kwargs.get("has_glow")
        self._has_glow = has_glow

        spider_type = kwargs.get("spider_type")
        self._spider_type = spider_type

        InvalidDataError.check_Y_value(is_operated, "has_batteries")

        InvalidDataError.check_none_or_empty_value(speed, "speed")
        InvalidDataError.check_none_or_empty_value(jump_height, "jump_height")
        InvalidDataError.check_none_or_empty_value(has_glow, "has_glow")

        InvalidDataError.check_non_negative_num(speed, "speed")
        InvalidDataError.check_non_negative_num(jump_height, "jump_height")
        InvalidDataError.check_Y_N_value(has_glow, "has_glow")
        InvalidDataError.check_in_enum(spider_type, SpiderTypes)

    @property
    def speed(self):
        return self._speed

    @property
    def jump_height(self):
        return self._jump_height

    @property
    def has_glow(self):
        return self._has_glow

    @property
    def spider_type(self):
        return self._spider_type

    def __str__(self):
        result = super().__str__()
        result += f", {self.speed}, {self.jump_height}, {self.has_glow}, {self.spider_type}"
        return result