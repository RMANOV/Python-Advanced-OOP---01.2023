# Operate
# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and 
# multiple numbers (integers) as additional arguments (*args). 
# The function should return the result of the operator applied to all the numbers.

def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
        return result
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
