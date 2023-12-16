import enum


class InvalidDataError(Exception):
    """
    Raised when the value of each column(attribute) is invalid.
    """
    def __init__(self, message):
        """
        Initialize an InvalidDataError object.
        :param message: a string
        """
        super().__init__("InvalidDataError - " + message)
        self._error_msg = message

    def get_error_msg(self):
        return self._error_msg

    @staticmethod
    def check_none_or_empty_value(value: str, attribute: str):
        """
        Checks if the given value is not none or empty.
        :param value: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is None or empty
        """
        if value is None or value == '':
            raise InvalidDataError(f"{attribute} should be included.")

    @staticmethod
    def check_same_value(value: str, comparable, attribute: str):
        """
        Checks if the given value is the same with the given comparable string.
        :param value: a string
        :param comparable: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is not the same with the given comparable
        """
        if value != comparable:
            raise InvalidDataError(f"{attribute} should be {comparable}.")

    @staticmethod
    def check_Y_N_value(value: str, attribute: str):
        """
        Checks if the given value is either 'Y' or 'N'.
        :param value: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is invalid
        """
        if value not in ['Y', 'N']:
            raise InvalidDataError(f"{attribute} should be either 'Y' or 'N'.")

    @staticmethod
    def check_Y_value(value: str, attribute: str):
        """
        Checks if the given value is 'Y'.
        :param value: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is invalid
        """
        if value != 'Y':
            raise InvalidDataError(f"{attribute} should be 'Y'.")

    @staticmethod
    def check_N_value(value: str, attribute: str):
        """
        Checks if the given value is 'N'.
        :param value: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is invalid
        """
        if value != 'N':
            raise InvalidDataError(f"{attribute} should be 'N'.")

    @staticmethod
    def check_non_negative_num(value: str, attribute: str):
        """
        Checks if the given value is a non-negative number.
        :param value: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is invalid
        """
        try:
            if int(value) < 0:
                raise InvalidDataError(f"{attribute} should be a non-negative number.")
        except ValueError:
            raise InvalidDataError(f"{attribute} should be a non-negative number.")

    @staticmethod
    def check_min_age(value: str, min_age: int):
        """
        Checks if the given value is greater than the min_age.
        :param value: a string
        :param min_age: an integer
        :raise InvalidDataError: raised when the given data is greater than the min_age
        """
        InvalidDataError.check_non_negative_num(value, "min_age")
        if int(value) < min_age:
            raise InvalidDataError(f"The minimum age should be greater than {min_age}.")

    @staticmethod
    def check_in_enum(value: str, members: enum):
        """
        Checks if the given value is in the enum list.
        :param value: a string
        :param members: an enum
        :raise InvalidDataError: raised when the given data doesn't exist in the enum.
        """
        if value not in [member.value for member in members]:
            raise InvalidDataError(f"{value} is an invalid attribute.")

    @staticmethod
    def check_negative_dimensions(dimensions: str, attribute: str):
        """
        Checks if the given value is a non-negative number.
        :param dimensions: a string
        :param attribute: a string
        :raise InvalidDataError: raised when the given data is invalid
        """
        dimensions = dimensions.split(',')
        try:
            if len(dimensions) != 2:
                InvalidDataError(f"{attribute} should consist of two non-negative numbers.")

            for dimension in dimensions:
                if float(dimension) < 0:
                    raise InvalidDataError(f"{attribute} should consist of two non-negative numbers.")
        except ValueError:
            raise InvalidDataError(f"{attribute} should consist of two non-negative numbers.")


class InsufficientStockError(Exception):
    """
    Raised when there is insufficient stock remaining.
    """
    def __init__(self):
        """
        Initialize an InsufficientStockError object.
        """
        super().__init__("Error: Insufficient Stock")
