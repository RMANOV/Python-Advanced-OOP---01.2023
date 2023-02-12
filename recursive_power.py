# Recursive Power
# Create a recursive function called recursive_power() which should receive a number and a power. 
# Using recursion, return the result of number ** power. 

def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)
