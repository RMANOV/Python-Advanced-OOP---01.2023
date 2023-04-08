# 5.	Class MainService
# In the main_service.py file, the class MainService should be implemented. Main service is a type of BaseService. Each main service has a capacity of 30.
# Methods
# __init__(name: str)
# •	In the __init__ method, all the needed attributes must be set.
# details()
# •	Returns a string in the following format:
# "{service_name} Main Service:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}"
# •	If the service doesn't have any robots, add "none" instead of the robots' names:
# "{service_name} Main Service:
# Robots: none"


from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {', '.join([r.name for r in self.robots])}"
        return f"{self.name} Main Service:\nRobots: none"
