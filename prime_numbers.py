# Prime Numbers
# Create a generator function called get_primes() which should receive a list of integer numbers and
# return a list containing only the prime numbers from the initial list.
# The function should use the yield keyword to return the prime numbers one by one.


def get_primes(numbers):
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number
