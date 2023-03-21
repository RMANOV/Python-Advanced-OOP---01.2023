# Take Halves
# You are given a skeleton with the following code:
# def solution():

#     def integers():
#         # TODO: Implement

#     def halves():

#         for i in integers():
#             # TODO: Implement

#     def take(n, seq):
#         # TODO: Implement

#     return (take, halves, integers)


# Implement the three generator functions:
# •	integers() - generates an infinite amount of integers (starting from 1)
# •	halves() - generates the halves of those integers (each integer / 2)
# •	take(n, seq) - takes the first n halves of those integers

# The solution should be a tuple of three functions: (take, halves, integers).
# The first function should be called take and should return a list of the first n elements from the given sequence.
# The second function should be called halves and should return a generator that generates the halves of the integers.
# The third function should be called integers and should return a generator that generates the integers.
# The solution should be a tuple of three functions: (take, halves, integers).

def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)
