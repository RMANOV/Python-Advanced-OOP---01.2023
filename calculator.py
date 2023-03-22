# Calculator
# Create a class called Calculator that has the following static methods:
# •	add(*args) - sums all the arguments passed to the function and returns the result
# •	multiply(*args) - multiplies all the numbers and returns the result
# •	divide(*args) - divides all the numbers (starting from the first one) and returns the result
# •	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result


class Calculator:
    def add(*args):
        return sum(args)

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result

    def divide(*args):
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

    def subtract(*args):
        result = args[0]
        for i in args[1:]:
            result -= i
        return result
