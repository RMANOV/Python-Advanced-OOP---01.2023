# Cup
# Create a class called Cup. Upon initialization, it should receive size (integer) and quantity 
# (an integer representing how much liquid is in it).
# The class should have two methods:
# •	fill(quantity) that will increase the amount of liquid in the cup with the given quantity 
# (if there is space in the cup, otherwise ignore).
# •	status() that will return the amount of free space left in the cup.


class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity
        return self.quantity

    def status(self):
        return self.size - self.quantity
