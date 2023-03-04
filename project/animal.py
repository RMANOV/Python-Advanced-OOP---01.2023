# The Animal class is a base class for any type of animal in the zoo. It should receive four public attributes - a name (string), a gender (str), an age (int), and a money_for_care (int) upon initialization.
# The Animal class should also have 1 additional method:
# •	__repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"
# The animal.py file should contain the following code:


class Animal:
    def __init__(self, name, gender, age, money_for_care):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
