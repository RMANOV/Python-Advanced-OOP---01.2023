# CRUD
# The abbreviation CRUD expands to Create, Read, Update and Delete.
# These are the four fundamental operations in a database.

# In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information.
# It consists of:
# •	Letters - on one or many positions in the table
# •	Numbers - on one or many positions in the table
# •	Empty positions - marked with "."

# Next, you will receive your first position on the table in the format "({row}, {column})"
# On the following lines, until you receive "Stop" you will be receiving commands in the format:
# •	"Create, {direction}, {value}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step in an empty position, create the given value on that position. E.g., 
# if the given value is "A", and the position is empty (".") - change it to "A"
# o	If the position is NOT empty, do NOT create a value on that position
# •	"Update, {direction}, {value}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, update the position with the given value. E.g., 
# if the given value is "h", and the position's value is "12" - change it to "h"
# o	If the position is empty, do NOT update the value on that position
# •	"Delete, {direction}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
# o	If the position is already empty, do NOT delete it
# •	"Read, {direction}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, print it on the console
# o	If the position is empty, do NOT read it
# You can make only ONE move at a time in the given direction for each command given.
# In the end, print the final matrix.
# Input
# •	On the first 6 lines - a matrix with positions separated by a single space
# o	Letters are in the range [a-zA-Z]
# o	Numbers are in the range [-100, 100]
# •	On the next line - your first position in the format: "({row}, {column})"
# •	On the following lines until you receive the command "Stop" - commands in the format shown above
# Output
# •	In the end, print the final matrix, each row on a new line, each position separated by a single space.
# Constraints
# •	You will always receive valid coordinates
# •	You will always receive directions in the range of the table
# •	You will always receive letters or numbers


matrix = [input().split() for _ in range(6)]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
row, col = map(int, input()[1:-1].split(", "))
while True:
    command = input()
    if command == "Stop":
        break

    if command.startswith("Create"):
        direction, value = command.split(", ")[1:]
        row += directions[direction][0]
        col += directions[direction][1]
        if 0 <= row < 6 and 0 <= col < 6 and matrix[row][col] == ".":
            matrix[row][col] = value

    elif command.startswith("Update"):
        direction, value = command.split(", ")[1:]
        row += directions[direction][0]
        col += directions[direction][1]
        if 0 <= row < 6 and 0 <= col < 6 and matrix[row][col] != ".":
            matrix[row][col] = value

    elif command.startswith("Delete"):
        direction = command.split(", ")[1]
        row += directions[direction][0]
        col += directions[direction][1]
        if 0 <= row < 6 and 0 <= col < 6 and matrix[row][col] != ".":
            matrix[row][col] = "."

    elif command.startswith("Read"):
        direction = command.split(", ")[1]
        row += directions[direction][0]
        col += directions[direction][1]
        if 0 <= row < 6 and 0 <= col < 6 and matrix[row][col] != ".":
            print(matrix[row][col])

for row in matrix:
    print(" ".join(row))
