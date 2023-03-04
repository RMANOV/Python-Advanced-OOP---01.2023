# The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class. Each of these animals costs a certain amount of money to be cared for:
# •	A lion needs 50
# •	A tiger needs 45
# •	A cheetah needs 60

from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)
