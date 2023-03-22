# The Worker class is a base class for any type of employee in the zoo. It should receive three public attributes - a name (string), an age (int), and a salary (int) upon initialization.
# The Worker class should also have one method:
# •	__repr__() - returns string representation of the workers in the format: "Name: {name}, Age: {age}, Salary: {salary}"
# The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.


from project.zoo import Zoo

class Worker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'