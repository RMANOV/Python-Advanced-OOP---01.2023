from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def make_sound(self):
        pass

    def feed(self, food):
        pass

    def __repr__(self):
        pass