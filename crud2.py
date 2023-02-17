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
