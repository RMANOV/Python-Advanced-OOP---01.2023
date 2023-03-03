# Create a Child class that inherits Person and has the same constructor definition. 
# However, do not copy the code from the Person class - reuse the Person class's constructor.

from project.person import Person

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
