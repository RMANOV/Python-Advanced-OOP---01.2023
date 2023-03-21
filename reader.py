# Reader
# Create a generator function called read_next() which should receive a different number of arguments (all iterable).
# On each iteration, the function should return each element from each sequence.

def read_next(*args):
    # Loop over each argument
    for arg in args:
        # Loop over each element in the argument
        for item in arg:
            # Yield the element
            yield item


# Test code
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')

# Output:
# string2dict

# Test code2
# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)

# Output2:
# N
# e
# e
# d
# 2
# 3
# words
# .
