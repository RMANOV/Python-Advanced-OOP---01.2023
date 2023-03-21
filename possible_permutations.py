# Possible permutations
# Create a generator function called possible_permutations() which should receive a list and
# return lists with all possible permutations between its elements.


import itertools

def possible_permutations(lst):
    # Use itertools.permutations to get an iterator of tuples
    perm_iter = itertools.permutations(lst)
    # Loop over each tuple
    for perm in perm_iter:
        # Yield the tuple as a list
        yield list(perm)
