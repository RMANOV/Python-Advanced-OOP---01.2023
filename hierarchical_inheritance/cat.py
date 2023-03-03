# •	Cat with a single method meow() that returns: "meowing..."
# Both Dog and Cat should inherit from Animal.


from project.animal import Animal


class Cat(Animal):
    def meow(self):
        return "meowing..."
