# Vowels
# Create a class called vowels, which should receive a string.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.


class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            current = self.string[self.index]
            self.index += 1
            if current in "aeiouAEIOU":
                return current
        raise StopIteration
