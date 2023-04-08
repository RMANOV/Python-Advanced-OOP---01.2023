# 2.	Class FemaleRobot
# In the female_robot.py file, the class FemaleRobot should be implemented. The female robot is a type of BaseRobot. Each female robot has 7 kilograms of weight initially.
# Methods
# __init__(name: str, kind: str, price: float)
# •	In the __init__ method, all the needed attributes must be set.
# eating()
# •	The method increases the robot's weight by 1 kilogram.

from project.robots.base_robot import BaseRobot

class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 7)

    def eating(self):
        self.weight += 1