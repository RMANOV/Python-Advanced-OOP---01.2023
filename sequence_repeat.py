# Sequence Repeat
# Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
# Implement an iterator to return the given elements, so they form a string with a length - the given number.
# If the number is greater than the number of elements, then the sequence repeats as necessary.

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.number:
            value = self.sequence[self.current % len(self.sequence)]
            self.current += 1
            return value
        raise StopIteration()