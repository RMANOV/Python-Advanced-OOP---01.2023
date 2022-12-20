# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. 
# Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) 
# until you receive the command "Start". Add those people to a queue. 
# Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. 
# Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".

import collections

water = int(input())
people = collections.deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break
    if command.startswith("refill"):
        water += int(command.split()[1])
    else:
        if water >= int(command):
            print(f"{people.popleft()} got water")
            water -= int(command)
        else:
            print(f"{people.popleft()} must wait")












# command = input()

# while not command == "Start":
#     command = input().split()
#     if len(command) == 1:
#         people.append(command[0])
#     else:
#         water += int(command[1])
#     if water <= 0:
#         print(f"{people.popleft()} must wait")
#     else:
#         print(f"{people.popleft()} got water")
#         water -= int(command[1])
# print(f"{water} liters left")