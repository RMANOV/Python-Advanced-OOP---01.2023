# •	SportsCar with a single method race() that returns: "racing...".
# SportsCar should inherit from Car and Car should inherit from Vehicle


from project.car import Car

class SportsCar(Car):
    def race(self):
        return "racing..."


