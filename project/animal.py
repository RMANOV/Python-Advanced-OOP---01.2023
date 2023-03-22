# Animals
# Your task is to create a class hierarchy like the one described below.
# Submit in judge a zip file named project, containing a separate file for each of the classes.
# The Animal class (abstract) should take, attributes, a name, an age, and a gender. It should have 2 methods: repr() and make_sound().
# The Dog class should inherit and implement the Animal class.
# Its repr() method should return "This is {name}. {name} is a {age} year old {gender} {class}". The dog sound is "Woof!".
# The Cat class should inherit and implement the Animal class.
# Its repr() method should return "This is {name}. {name} is a {age} year old {gender} {class}". The cat sound, "Meow meow!".
# The Kitten class should inherit and implement the Cat class.
# Its gender is "Female", and its sound is "Meow".
# The Tomcat class should inherit and implement the Cat class.
# Its gender is "Male", and its sound is "Hiss".

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
