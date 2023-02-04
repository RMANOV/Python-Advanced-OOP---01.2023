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
position = None
for i in range(5):
    if "A" in field[i]:
        position = (i, field[i].index("A"))
        break

targets_hit = []
commands = int(input())
for _ in range(commands):
    if len(commands) < 3:
        cmd, direction = input().split()
        steps = 1
    else:
        cmd, direction, steps = input().split()
    steps = int(steps)
    if cmd == "move":
        if direction == "up":
            new_position = (position[0] - steps, position[1])
        elif direction == "down":
            new_position = (position[0] + steps, position[1])
        elif direction == "left":
            new_position = (position[0], position[1] - steps)
        elif direction == "right":
            new_position = (position[0], position[1] + steps)
        if (
            0 <= new_position[0] < 5
            and 0 <= new_position[1] < 5
            and field[new_position[0]][new_position[1]] == "."
        ):
            position = new_position
    else:
        if direction == "up":
            for i in range(position[0] - 1, -1, -1):
                if field[i][position[1]] == "x":
                    targets_hit.append(f"[{i}, {position[1]}]")
                    field[i][position[1]] = "."
                    break
        elif direction == "down":
            for i in range(position[0] + 1, 5):
                if field[i][position[1]] == "x":
                    targets_hit.append(f"[{i}, {position[1]}]")
                    field[i][position[1]] = "."
                    break
        elif direction == "left":
            for i in range(position[1] - 1, -1, -1):
                if field[position[0]][i] == "x":
                    targets_hit.append(f"[{position[0]}, {i}]")
                    field[position[0]][i] = "."
                    break
        elif direction == "right":
            for i in range(position[1] + 1, 5):
                if field[position[0]][i] == "x":
                    targets_hit.append(f"[{position[0]}, {i}]")
                    field[position[0]][i] = "."
                    break

if targets_hit:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {sum(row.count('x') for row in field)} targets left.")

print(*targets_hit, sep=" ")
