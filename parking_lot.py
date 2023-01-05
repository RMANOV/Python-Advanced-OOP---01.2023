# Parking Lot
# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N. 
# On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". 
# The direction could only be "IN" or "OUT". 
# Print the car numbers which are still in the parking lot. 
# Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".

number_of_commands = int(input())
parking_lot = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")