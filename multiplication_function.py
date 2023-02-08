# 1.	Multiplication Function
# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and returns the result of the multiplication of all of them. 
# Submit only your function in the Judge system.

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

multiply(int(x) for x in input().split(", "))
