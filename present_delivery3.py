count_presents = int(input())
size_neighborhood = int(input())
matrix = [[x for x in input().split()] for _ in range(size_neighborhood)]
santa_position = [
    [i, j]
    for i in range(size_neighborhood)
    for j in range(size_neighborhood)
    if matrix[i][j] == "S"
][0]

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

while True:
    command = input()
    if command == "Christmas morning":
        break
    santa_position[0] += directions[command][0]
    santa_position[1] += directions[command][1]
    if matrix[santa_position[0]][santa_position[1]] == "V":
        if count_presents > 0:
            count_presents -= 1
        matrix[santa_position[0]][santa_position[1]] = "-"
    elif matrix[santa_position[0]][santa_position[1]] == "X":
        matrix[santa_position[0]][santa_position[1]] = "-"
    elif matrix[santa_position[0]][santa_position[1]] == "C":
        matrix[santa_position[0]][santa_position[1]] = "-"
        for i in range(santa_position[0] - 1, santa_position[0] + 2):
            for j in range(santa_position[1] - 1, santa_position[1] + 2):
                if 0 <= i < size_neighborhood and 0 <= j < size_neighborhood:
                    if matrix[i][j] == "V" and count_presents > 0:
                        count_presents -= 1
                    matrix[i][j] = "-"
    if count_presents <= 0:
        break

if count_presents <= 0 and any("V" in row for row in matrix):
    print("Santa ran out of presents!")
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"No presents for {sum(row.count('V') for row in matrix)} nice kid/s.")

elif count_presents > 0 and not any("V" in row for row in matrix):
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"Good job, Santa! {sum(row.count('V') for row in matrix)} happy nice kid/s.")

elif count_presents <= 0 and not any("V" in row for row in matrix):
    print("Santa ran out of presents!")
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"No presents for {sum(row.count('V') for row in matrix)} nice kid/s.")

elif count_presents > 0 and any("V" in row for row in matrix):
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"Good job, Santa! {sum(row.count('V') for row in matrix)} happy nice kid/s.")
