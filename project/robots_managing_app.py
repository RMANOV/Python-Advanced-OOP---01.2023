# 7.	Class RobotsManagingApp
# In the robots_managing_app.py file, the class RobotsManagingApp should be implemented. It will contain the functionality of the project.
# Structure
# The class should have the following attributes:
# •	robots: list
# o	Empty list that will contain all robots (objects) that are created.
# •	services: list
# o	Empty list that will contain all services (objects) that are created.
# Methods
# __init__()
# •	In the __init__ method, all the needed attributes must be set.
# add_service(service_type: str, name: str)
# The method creates a service of the given type and adds it to the services collection. 
# All service names will be unique.
# •	If the service type is not valid, raise an Exception with the following message:
# "Invalid service type!"
# •	Otherwise, create the service, add it to the services list, and return the following message:
# "{service_type} is successfully added."
# •	Valid types of services are: "MainService" and "SecondaryService"
# add_robot(robot_type: str, name: str, kind: str, price: float)
# The method creates a robot of the given type and adds it to the robots' collection. 
# All robots' names will be unique.
# •	If the robot type is not valid, raise an Exception with the following message:
# "Invalid robot type!"
# •	Otherwise, create the robot, add it to the robots' list, and return the following message:
# "{robot_type} is successfully added."
# •	Valid types of robots are: "MaleRobot" and "FemaleRobot"
# add_robot_to_service(robot_name: str, service_name: str)
# The method adds the robot with the given name to the service if there is a capacity for that. Both robot and service with the given names will always exist.
# •	First, check if the robot can be added to the service. The Female robot can be ONLY added to the Secondary Service and the Male robot can be ONLY added to the Main Service. In case of a mismatch, return the message: "Unsuitable service."
# •	Next, if there is NOT enough capacity to add the robot to the service, raise an Exception with the following message: "Not enough capacity for this robot!"
# •	If the robot can be added successfully to the service, remove it from the robots' collection, and add it to the service. Return the following message: "Successfully added {robot_name} to {service_name}."
# remove_robot_from_service(robot_name: str, service_name: str)
# The method removes the robot with the given name from the service. The service with the given name will always exist.
# •	Check if there is a robot with the given name in the service. If not, raise an Exception with the following message: "No such robot in this service!"
# •	If the robot can be removed successfully from the service, remove it from the service, and add it back to the robots' collection. Return the following message: "Successfully removed {robot_name} from {service_name}."
# feed_all_robots_from_service(service_name: str)
# The method feeds all robots from the service. The service with the given name will always exist. When all robots from the service are successfully fed (hint: use eating() method), return the following message: 
# "Robots fed: {number_of_robots_fed}."
# service_price(service_name: str)
# The method calculates the price of all robots that are in the service. The service with the given name will always exist. 
# Return the calculated price, formatted to the second decimal place with the following message:
# "The value of service {service_name} is {total_price}."
# __str__()
# Returns information about each service (hint: you can use the service details() method)
# "{service_name1} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# {service_name2} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# …
# {service_nameN} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}"

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")
        
        service = Service(name, service_type)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        robot = Robot(name, kind, price, robot_type)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if robot.robot_type == "FemaleRobot" and service.service_type != "SecondaryService":
            return "Unsuitable service."
        elif robot.robot_type == "MaleRobot" and service.service_type != "MainService":
            return "Unsuitable service."

        if not service.add_robot(robot):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)

        if not service.remove_robot(robot_name):
            raise Exception("No such robot in this service!")

        robot = service.get_robot(robot_name)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)
        number_of_robots_fed = service.feed_all_robots()
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)
        total_price = service.calculate_price()
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)
