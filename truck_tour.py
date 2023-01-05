# There is a circle road with N petrol pumps. 
# The petrol pumps are numbered 0 to (N−1) (both inclusive). 
# For each petrol pump, you will receive two pieces of information (separated by a single space): 
# -	The amount of petrol the petrol pump will give you
# -	The distance from that petrol pump to the next petrol pump (kilometers)
# You are a truck driver, and you want to go all around the circle. 
# You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
# In the beginning, the tank is empty, 
# but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. 
# You never miss filling its tank at a petrol pump.
# Input
# •	On the first line, you will receive the number of petrol pumps - N
# •	On the next N lines, 
# you will receive the amount of petrol that each petrol pump will give and the distance between that petrol pump and the next petrol pump, separated by a single space
# Output
# •	An integer which will be the smallest index of a petrol pump from which you can start the tour
# Constraints
# •	1 ≤ N ≤ 1000001
# •	1 ≤ amount of petrol, distance ≤ 1000000000
# •	You will always have at least one point from where the truck will be able to complete the circle


number_of_petrol_pumps = int(input())
queue = []

for i in range(number_of_petrol_pumps):
    amount, distance = map(int, input().split())
    queue.append((amount, distance))

petrol = 0
index = 0

while queue:
    amount, distance = queue.pop(0)
    petrol += amount
    petrol -= distance
    if petrol < 0:
        petrol = 0
        index = (index + 1) % number_of_petrol_pumps
    else:
        index = (index + 1) % number_of_petrol_pumps
    queue.append((amount, distance))

print(index)





# number_of_petrol_pumps = int(input())
# petrol_pumps = []
# minimum = 0

# for i in range(number_of_petrol_pumps):
#     amount, distance = map(int, input().split())
#     petrol_pumps.append((amount, distance))

# for i, (amount, distance) in enumerate(petrol_pumps):
#     petrol = amount
#     for j in range(i, i + number_of_petrol_pumps):
#         petrol -= distance
#         next_pump = (j + 1) % number_of_petrol_pumps
#         petrol += petrol_pumps[next_pump][0]
#         minimum = min(minimum, petrol)
#         if petrol < 0:
#             break
#     else:
#         print(minimum)
#         # print(i)
#         break














# for i in range(number_of_petrol_pumps):
#     petrol_pump = input().split()
#     petrol_pump = [int(x) for x in petrol_pump]
#     petrol_pump.append(petrol_pump[0] - petrol_pump[1])
#     petrol_pump.pop(0)
#     petrol_pump.pop(0)
#     if i == 0:
#         petrol_pump.append(petrol_pump[0])
#         petrol_pump.pop(0)
#     else:
#         petrol_pump.append(petrol_pump[0] + petrol_pump[1])
#         petrol_pump.pop(0)
#         petrol_pump.pop(0)
#     if i == 0:
#         petrol_pump.append(petrol_pump[0])
#         petrol_pump.pop(0)
#     else:
#         petrol_pump.append(petrol_pump[0] + petrol_pump[1])
#         petrol_pump.pop(0)
#         petrol_pump.pop(0)
#     if petrol_pump[0] >= 0 and petrol_pump[1] >= 0:
#         print(i)
#         break
