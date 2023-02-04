# 6.    Range Day
# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •    Your position is marked with the symbol "A"
# •    Targets marked with symbol "x"
# •    All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •    "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
# You can only move if the field you want to step on is marked with ".".
# •    "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets,
# and you cannot reach them - you can shoot only the nearest target. When you have shot a target,
# the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •    If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# •    If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •    5 lines representing the field (symbols, separated by a single space)
# •    N - count of commands
# •    On the following N lines - the commands in the format described above
# Output
# •    On the first line, print one of the following:
# o    If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o    Otherwise:
# "Training not completed! {count_left_targets} targets left."
# •    Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.

field = [input().split() for _ in range(5)]
count_of_commands = int(input())
position = [[i, field[i].index("A")] for i in range(5) if "A" in field[i]][0]

directions = { "right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0) }

commands = { "move": lambda x, y, z: (x + directions[y][0], y + directions[y][1], z),
            'shoot': lambda x, y, z: (x + directions[y][0], y + directions[y][1], z + 1) }

shooted_targets = []

for _ in range(count_of_commands):
    command = input().split()
    if command[0] == "move":
        position = commands[command[0]](*position, int(command[2]))
    elif command[0] == "shoot":
        position = commands[command[0]](*position, 0)
    if 0 <= position[0] < 5 and 0 <= position[1] < 5:
        if field[position[0]][position[1]] == "x":
            field[position[0]][position[1]] = "."
            shooted_targets.append(f"[{position[0]}, {position[1]}]")
    else:
        position = commands[command[0]](*position, -1)

if not shooted_targets:
    print(f"Training completed! All {count_of_commands} targets hit.")
else:
    print(f"Training not completed! {count_of_commands - len(shooted_targets)} targets left.")
    print(*shooted_targets, sep=' ')












# for i in range(5):
#     if "A" in field[i]:
#         position = (i, field[i].index("A"))
#         break
# targets = 0
# for _ in range(count_of_commands):
#     command = input().split()
#     if command[0] == "move":
#         direction = command[1]
#         steps = int(command[2])
#         if direction == "right":
#             if (
#                 position[1] + steps < 5
#                 and field[position[0]][position[1] + steps] == "."
#             ):
#                 field[position[0]][position[1]] = "."
#                 position = (position[0], position[1] + steps)
#                 field[position[0]][position[1]] = "A"
#         elif direction == "left":
#             if (
#                 position[1] - steps >= 0
#                 and field[position[0]][position[1] - steps] == "."
#             ):
#                 field[position[0]][position[1]] = "."
#                 position = (position[0], position[1] - steps)
#                 field[position[0]][position[1]] = "A"
#         elif direction == "up":
#             if (
#                 position[0] - steps >= 0
#                 and field[position[0] - steps][position[1]] == "."
#             ):
#                 field[position[0]][position[1]] = "."
#                 position = (position[0] - steps, position[1])
#                 field[position[0]][position[1]] = "A"
#         elif direction == "down":
#             if (
#                 position[0] + steps < 5
#                 and field[position[0] + steps][position[1]] == "."
#             ):
#                 field[position[0]][position[1]] = "."
#                 position = (position[0] + steps, position[1])
#                 field[position[0]][position[1]] = "A"
#     elif command[0] == "shoot":
#         direction = command[1]
#         if direction == "right":
#             for i in range(position[1] + 1, 5):
#                 if field[position[0]][i] == "x":
#                     field[position[0]][i] = "."
#                     targets += 1
#                     break
#         elif direction == "left":
#             for i in range(position[1] - 1, -1, -1):
#                 if field[position[0]][i] == "x":
#                     field[position[0]][i] = "."
#                     targets += 1
#                     break
#         elif direction == "up":
#             for i in range(position[0] - 1, -1, -1):
#                 if field[i][position[1]] == "x":
#                     field[i][position[1]] = "."
#                     targets += 1
#                     break
#         elif direction == "down":
#             for i in range(position[0] + 1, 5):
#                 if field[i][position[1]] == "x":
#                     field[i][position[1]] = "."
#                     targets += 1
#                     break
# if targets == 15:
#     print(f"Training completed! All {targets} targets hit.")
# else:
#     print(f"Training not completed! {15 - targets} targets left.")
#     for i in range(5):
#         for j in range(5):
#             if field[i][j] == "x":
#                 print(f"[{i}, {j}]")
