# Countdown Iterator
# Create a class called countdown_iterator. Upon initialization, it should receive a count.
# Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.


class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        raise StopIteration()