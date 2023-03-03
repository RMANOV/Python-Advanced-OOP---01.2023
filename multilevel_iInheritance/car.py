# •	Car with a single method drive() that returns: "driving..."
# •	SportsCar with a single method race() that returns: "racing...". 
# SportsCar should inherit from Car and Car should inherit from Vehicle

from project.vehicle import Vehicle

class Car(Vehicle):
    def drive(self):
        return "driving..."



