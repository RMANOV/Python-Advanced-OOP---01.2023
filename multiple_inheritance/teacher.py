# •	Teacher with a single method teach() that returns: "teaching...". 
# Teacher should inherit from Person and Employee.

from project.person import Person
from project.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
