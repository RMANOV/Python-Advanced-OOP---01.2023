# Zoo
# Create a zoo project that contains the following classes: 
# Animal: Mammal, Reptile
# mammal: gorilla, bear
# Reptile: snake, lizard
# Submit in judge a zip file of the project, containing a separate file for each of the classes using the structure shown below:
 
# Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another class, as shown in the diagram. 
# The Animal class should receive a name - string upon initialization.


class Animal:
    def __init__(self, name):
        self.name = name
