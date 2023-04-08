# 1.	 Class BaseRobot
# In the base_robot.py file, the class BaseRobot should be implemented. It is a base class for any type of robot, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes: 
# •	name: str
# o	The value represents the name of the robot.
# o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Robot name cannot be empty!"
# •	kind: str
# o	The value represents the kind of the robot.
# o	If the kind is an empty string or contains only white spaces, raise a ValueError with the message: "Robot kind cannot be empty!"
# •	price: float
# o	The value represents the price of the robot.
# o	If the price is less than or equal to 0.0, raise a ValueError with the message: "Robot price cannot be less than or equal to 0.0!"
# •	weight: int
# o	The value represents the weight in kilograms of the robot.
# Methods
# __init__(name: str, kind: str, price: float, weight: int)
# •	In the __init__ method, all the needed attributes must be set.
# eating()
# •	The method increases the robot's kilograms. Keep in mind that each kind of robot implements the method differently.

from abc import ABC, abstractmethod

class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        if not name.strip():
            raise ValueError("Robot name cannot be empty!")
        if not kind.strip():
            raise ValueError("Robot kind cannot be empty!")
        if price <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")

        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @abstractmethod
    def eating(self):
        """
        The method increases the robot's kilograms.
        Each kind of robot implements the method differently.
        """
        pass
