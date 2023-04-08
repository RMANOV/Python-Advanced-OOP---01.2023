# 6.	Class SecondaryService
# In the secondary_service.py file, the class SecondaryService should be implemented. Secondary service is a type of BaseService. Each secondary service has a capacity of 15.
# Methods
# __init__(name: str)
# •	In the __init__ method, all the needed attributes must be set.
# details()
# •	Returns a string in the following format:
# "{service_name} Secondary Service:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}"
# •	If the service doesn't have any robots, add "none" instead of the robots' names:
# "{service_name} Secondary Service:
# Robots: none"

from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\nRobots: {', '.join([r.name for r in self.robots])}"
        return f"{self.name} Secondary Service:\nRobots: none"
