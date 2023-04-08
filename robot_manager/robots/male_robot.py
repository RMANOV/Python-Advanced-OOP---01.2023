# 3.	Class MaleRobot
# In the male_robot.py file, the class MaleRobot should be implemented. The male robot is a type of BaseRobot. Each male robot has 9 kilograms of weight initially.
# Methods
# __init__(name: str, kind: str, price: float)
# •	In the __init__ method, all the needed attributes must be set.
# eating()
# •	The method increases the robot's weight by 3 kilograms.

from project.robots.base_robot import BaseRobot

class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)

    def eating(self):
        self.weight += 3
