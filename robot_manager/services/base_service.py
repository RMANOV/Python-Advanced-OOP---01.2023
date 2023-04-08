# 4.	Class BaseService
# In the base_service.py file, the class BaseService should be implemented. It is a base class for any type of service, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes: 
# •	name: str
# o	The value represents the name of the service.
# o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Service name cannot be empty!"
# •	capacity: int
# o	The value represents the number of robots а service can have.
# o	If the capacity is less than or equal to 0, raise a ValueError with the message: "Service capacity cannot be less than or equal to 0!"
# •	robots: list
# o	Empty list that will contain robots (objects) added to the service.
# Methods
# __init__(name: str, capacity: int)
# •	In the __init__ method, all the needed attributes must be set.
# details()
# •	Returns a string with information about the service depending on its type.

from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name.strip()
        if self.name == "":
            raise ValueError("Service name cannot be empty!")

        self.capacity = capacity
        if self.capacity <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.robots = []

    @abstractmethod
    def details(self):
        """
        Returns a string with information about the service depending on its type.

        :return: A string with information about the service
        """
        pass
