# Squares
# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).


def squares(n):
    for i in range(1, n + 1):
        yield i * i

