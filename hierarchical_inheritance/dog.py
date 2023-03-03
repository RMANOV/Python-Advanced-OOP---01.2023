# •	Dog with a single method bark() that returns: "barking..."
# •	Cat with a single method meow() that returns: "meowing..."
# Both Dog and Cat should inherit from Animal.

from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."
