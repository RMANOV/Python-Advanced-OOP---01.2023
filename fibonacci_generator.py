# Fibonacci Generator
# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
# The first two numbers in the sequence are always 0 and 1.
# Each following Fibonacci number is created by the sum of the current number with the previous one.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b