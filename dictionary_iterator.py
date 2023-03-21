# Dictionary Iterator
# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.keys):
            key = self.keys[self.current]
            value = self.dictionary[key]
            self.current += 1
            return key, value
        raise StopIteration()