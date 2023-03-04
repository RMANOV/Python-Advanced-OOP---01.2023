# Wild Cat Zoo
# Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole project folder/module) - it is important to include all files in the project module to make proper imports.

# The Animal class is a base class for any type of animal in the zoo. It should receive four public attributes - a name (string), a gender (str), an age (int), and a money_for_care (int) upon initialization.
# The Animal class should also have 1 additional method:
# •	__repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"
# The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class. Each of these animals costs a certain amount of money to be cared for:
# •	A lion needs 50
# •	A tiger needs 45
# •	A cheetah needs 60
# The Worker class is a base class for any type of employee in the zoo. It should receive three public attributes - a name (string), an age (int), and a salary (int) upon initialization.
# The Worker class should also have one method:
# •	__repr__() - returns string representation of the workers in the format: "Name: {name}, Age: {age}, Salary: {salary}"
# The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.
# The Zoo class should receive 4 attributes upon initialization:
# •	Public attribute name: string
# •	Private attribute budget: int
# •	Private attribute animal_capacity: int
# •	Private attribute workers_capacity: int
# It should also have 2 instance attributes:
# •	Public attribute animals: list - (empty upon initialization)
# •	Public attribute workers: list - (empty upon initialization)
# The Zoo class should also have 8 methods:
# •	add_animal(animal, price)
# o	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list, reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
# o	If you have the capacity, but no budget, return "Not enough budget"
# o	In any other case, you do not have space, and you should return "Not enough space for animal"
# •	hire_worker(worker)
# o	If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
# o	Otherwise, return "Not enough space for worker"
# •	fire_worker(worker_name)
# o	If there is a worker with that name in the workers' list, remove him and return "{worker_name} fired successfully"
# o	Otherwise, return "There is no {worker_name} in the zoo"
# •	pay_workers()
# o	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"
# o	Otherwise, return "You have no budget to pay your workers. They are unhappy"
# •	tend_animals()
# o	If you have enough budget to take care of the animals, reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"
# o	Otherwise, return "You have no budget to tend the animals. They are unhappy."
# •	profit(amount)
# o	Increase the budget with the given amount of profit
# •	animals_status()
# o	Returns the following string (Hint: use the __repr__ methods of the animals to print them on the console):
# "You have {total_animals_count} animals
# ----- {amount_of_lions} Lions:
# {lion1}
# …
# {lionN}
# ----- {amount_of_tigers} Tigers:
# {tiger1}
# …
# {tigerN}
# ----- {amount_of_cheetahs} Cheetahs:
# {cheetah1}
# …
# {cheetahN}"
# •	workers_status()
# o	Returns the following string (Hint: use the __repr__ methods of the workers to print them on the console):
# "You have {total_workers_count} workers
# ----- {amount_of_keepers} Keepers:
# {keeper1}
# …
# {keeperN}
# ----- {amount_of_caretakers} Caretakers:
# {caretaker1}
# …
# {caretakerN}
# ----- {amount_of_vetes} Vets:
# {vet1}
# …
# {vetN}"

# The main.py file should contain the following code:
# from zoo import Zoo
# from animal import Lion, Tiger, Cheetah

from project.animal import Lion, Tiger, Cheetah
from project.worker import Keeper, Caretaker, Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_tend:
            self.__budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if type(animal).__name__ == "Lion"]
        tigers = [animal for animal in self.animals if type(animal).__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if type(animal).__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals"
        result += f" ----- {len(lions)} Lions: {' '.join([str(lion) for lion in lions])}"
        result += f" ----- {len(tigers)} Tigers: {' '.join([str(tiger) for tiger in tigers])}"
        result += f" ----- {len(cheetahs)} Cheetahs: {' '.join([str(cheetah) for cheetah in cheetahs])}"
        return result + " " if result.endswith(" ") else result

    def workers_status(self):
        keepers = [worker for worker in self.workers if type(worker).__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if type(worker).__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if type(worker).__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers"
        result += f" ----- {len(keepers)} Keepers: {' '.join([str(keeper) for keeper in keepers])}"
        result += f" ----- {len(caretakers)} Caretakers: {' '.join([str(caretaker) for caretaker in caretakers])}"
        result += f" ----- {len(vets)} Vets: {' '.join([str(vet) for vet in vets])}"
        return result + " " if result.endswith(" ") else result
