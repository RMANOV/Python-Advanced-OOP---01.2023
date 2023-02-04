# Present Delivery
# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
# with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
# If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V".
# There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive.
# If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid,
# he doesn't drop a present. If the command sends Santa to a cell marked with "C",
# Santa eats cookies and becomes happy and extra generous to all the kids around him*
# (meaning all of them will receive presents - it doesn't matter if naughty or nice).
# If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case,
# Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# •	On the first line, you are given the integer m - the count of presents
# •	On the second - integer n - the size of the neighborhood
# •	The following n lines hold the values for every row
# •	On each of the following lines you will get a command
# Output
# •	On the first line:
# o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# •	Next, print the matrix.
# •	In the end, print one of these messages:
# o	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# o	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."


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
nice_kids = 0
naughty_kids = 0
cookies = 0


while True:
    command = input()
    if command == "Christmas morning":
        break
    if not (0 <= santa_position[0] + directions[command][0] < size_neighborhood) or not (
        0 <= santa_position[1] + directions[command][1] < size_neighborhood
    ):
        continue
    if matrix[santa_position[0] + directions[command][0]][
        santa_position[1] + directions[command][1]
    ] == "-":
        continue
    
    santa_position[0] += directions[command][0]
    santa_position[1] += directions[command][1]
    if matrix[santa_position[0]][santa_position[1]] == "V":
        count_presents -= 1
        nice_kids += 1
        matrix[santa_position[0]][santa_position[1]] = "-"
    elif matrix[santa_position[0]][santa_position[1]] == "X":
        naughty_kids += 1
        matrix[santa_position[0]][santa_position[1]] = "-"
    elif matrix[santa_position[0]][santa_position[1]] == "C":
        cookies += 1
        matrix[santa_position[0]][santa_position[1]] = "-"
        for i in range(santa_position[0] - 1, santa_position[0] + 2):
            for j in range(santa_position[1] - 1, santa_position[1] + 2):
                if 0 <= i < size_neighborhood and 0 <= j < size_neighborhood:
                    if matrix[i][j] == "V":
                        count_presents -= 1
                        nice_kids += 1
                    matrix[i][j] = "-"
    if count_presents <= 0:
        break

if count_presents <= 0 and any("V" in row for row in matrix):
    print("Santa ran out of presents!")
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"No presents for {nice_kids} nice kid/s.")
elif count_presents <= 0 and not any("V" in row for row in matrix):
    print("Santa ran out of presents!")
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
elif count_presents > 0 and not any("V" in row for row in matrix):
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
elif count_presents > 0 and any("V" in row for row in matrix):
    print(*[" ".join(row) for row in matrix], sep="\n")
    print(f"No presents for {nice_kids} nice kid/s.")






# while True:
#     command = input()
#     if command == "Christmas morning":
#         break
#     santa_position[0] += directions[command][0]
#     santa_position[1] += directions[command][1]
#     if matrix[santa_position[0]][santa_position[1]] == "V":
#         count_presents -= 1
#         matrix[santa_position[0]][santa_position[1]] = "-"
#     elif matrix[santa_position[0]][santa_position[1]] == "X":
#         matrix[santa_position[0]][santa_position[1]] = "-"
#     elif matrix[santa_position[0]][santa_position[1]] == "C":
#         matrix[santa_position[0]][santa_position[1]] = "-"
#         for i in range(santa_position[0] - 1, santa_position[0] + 2):
#             for j in range(santa_position[1] - 1, santa_position[1] + 2):
#                 if 0 <= i < size_neighborhood and 0 <= j < size_neighborhood:
#                     if matrix[i][j] == "V":
#                         count_presents -= 1
#                     matrix[i][j] = "-"
#     if count_presents <= 0:
#         break

# if count_presents <= 0 and any("V" in row for row in matrix):
#     print("Santa ran out of presents!")
#     print(*[" ".join(row) for row in matrix], sep="\n")
#     print(f"No presents for {sum(nau_kids)} nice kid/s.")
# elif count_presents > 0 and any("V" in row for row in matrix):
#     print("Good job, Santa! {count_nice_kids} happy nice kid/s.")
#     print(*[" ".join(row) for row in matrix], sep="\n")
#     print(f"No presents for {sum(nau_kids)} nice kid/s.")


# while True:
#     command = input()
#     if command == "Christmas morning":
#         break
#     santa_position[0] += directions[command][0]
#     santa_position[1] += directions[command][1]
#     if matrix[santa_position[0]][santa_position[1]] == "V":
#         count_presents -= 1
#         matrix[santa_position[0]][santa_position[1]] = "-"
#     elif matrix[santa_position[0]][santa_position[1]] == "X":
#         matrix[santa_position[0]][santa_position[1]] = "-"
#     elif matrix[santa_position[0]][santa_position[1]] == "C":
#         matrix[santa_position[0]][santa_position[1]] = "-"
#         for i in range(santa_position[0] - 1, santa_position[0] + 2):
#             for j in range(santa_position[1] - 1, santa_position[1] + 2):
#                 if 0 <= i < size_neighborhood and 0 <= j < size_neighborhood:
#                     if matrix[i][j] == "V":
#                         count_presents -= 1
#                     matrix[i][j] = "-"
#     if count_presents <= 0:
#         break

# if count_presents <= 0 and any("V" in row for row in matrix):
#     print("Santa ran out of presents!")
#     print(*[" ".join(row) for row in matrix], sep="\n")
#     print(f"No presents for {sum(row.count('V') for row in matrix)} nice kid/s.")

# elif count_presents > 0 and not any("V" in row for row in matrix):
#     print(*[" ".join(row) for row in matrix], sep="\n")
#     print(f"Good job, Santa! {sum(row.count('V') for row in matrix)} happy nice kid/s.")

# elif count_presents <= 0 and not any("V" in row for row in matrix):
#     print("Santa ran out of presents!")
#     print(*[" ".join(row) for row in matrix], sep="\n")
#     print(f"Good job, Santa! {sum(row.count('V') for row in matrix)} happy nice kid/s.")
