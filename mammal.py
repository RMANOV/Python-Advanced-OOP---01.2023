# Mammal
# Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound.
# Create a class attribute called kingdom which should not be accessed outside the class and set it to be "animals".
# Create three more instance methods:
# •	make_sound() - returns a string in the format "{name} makes {sound}"
# •	get_kingdom() - returns the private kingdom attribute
# •	info() - returns a string in the format "{name} is of type {type}"

class Mammal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"