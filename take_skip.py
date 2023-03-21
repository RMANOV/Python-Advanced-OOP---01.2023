# Take Skip
# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
# Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.


class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            value = self.current * self.step
            self.current += 1
            return value
        raise StopIteration()