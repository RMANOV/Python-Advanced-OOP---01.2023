# Vet
# Create a class called Vet. Upon initialization, it should receive a name (string).
# It should also have an instance attribute called animals (empty list by default).
# There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets;
# and space (5 by default). You should create 3 additional instance methods:
# -	register_animal(animal_name)
# o	If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
# o	Otherwise, returns "Not enough space"
# -	unregister_animal(animal_name)
# o	If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
# o	Otherwise, returns "{animal} not in the clinic"
# -	info()
# o	Returns info about the vet, the number of animals in his list and the free space in the clinic:
# "{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(self.animals) < self.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self.space - len(self.animals)} space left in clinic"
