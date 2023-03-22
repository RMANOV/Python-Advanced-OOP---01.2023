# Hotel Rooms
# In a folder called project create two files: hotel.py and room.py
# In the room.py file, create a class called Room. 
# Upon initialization, it should receive a number (int) and a capacity (int). 
# It should also have an attribute called guests (0 by default) and is_taken (False by default). 
# The class should have 2 additional methods:
# •	take_room(people) - if the room is not taken, and there is enough space, the guests take the room. 
# Otherwise, the method should return "Room number {number} cannot be taken"
# •	free_room() - if the room is taken, free it. Otherwise, return "Room number {number} is not taken"
# In the hotel.py file, create a class called Hotel. Upon initialization, it should receive a name (str). 
# It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default). The class should have 5 more methods:
# •	from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
# •	add_room(room: Room) - adds the room to the list of rooms
# •	take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
# •	free_room(room_number) - finds the room with that number and tries to free it
# •	status() - returns information about the hotel in the following format:
# "Hotel {name} has {guests} total guests
# Free rooms: {numbers of all free rooms separated by comma and space}
# Taken rooms: {numbers of all taken rooms separated by comma and space}"

from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if result.startswith("Room number"):
            self.guests += people
        return result

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.free_room()
        if result.startswith("Room number"):
            self.guests -= room.guests
        return result

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
