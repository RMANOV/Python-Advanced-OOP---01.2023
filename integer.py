# Integer
# Create a class called Integer. Upon initialization, it should receive a single parameter value (int).
# It should have 3 additional methods:
# •	from_float(float_value) - creates a new instance by flooring the provided floating number.
# If the value is not a float, return a message "value is not a float"
# •	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
# •	from_string(value) - creates a new instance by converting the string to an integer (if the value cannot be converted,
# return a message "wrong type")


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) == float:
            return cls(int(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(value)):
            if i > 0 and roman_to_int[value[i]] > roman_to_int[value[i - 1]]:
                result += roman_to_int[value[i]] - 2 * roman_to_int[value[i - 1]]
            else:
                result += roman_to_int[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            return cls(int(value))
        return "wrong type"




    # def from_float(self, float_value):
    #     if type(float_value) == float:
    #         return int(float_value)
    #     return "value is not a float"

    # def from_roman(self, value):
    #     roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #     result = 0
    #     for i in range(len(value)):
    #         if i > 0 and roman_to_int[value[i]] > roman_to_int[value[i - 1]]:
    #             result += roman_to_int[value[i]] - 2 * roman_to_int[value[i - 1]]
    #         else:
    #             result += roman_to_int[value[i]]
    #     return result

    # def from_string(self, value):
    #     if type(value) == str:
    #         return int(value)
    #     return "wrong type"

    # def __str__(self):
    #     return f"{self.value}"
