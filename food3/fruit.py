# •	In the fruit.py file, create a class called Fruit, with will receive a name(str) and an expiration_date(str) upon initialization.
# Fruit should inherit from Food.

from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = str(name)
        self.expiration_date = str(expiration_date)
