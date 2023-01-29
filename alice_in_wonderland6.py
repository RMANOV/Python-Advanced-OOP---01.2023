# Alice in Wonderland
# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,
# you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers.
# If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting.
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command
# Output
# •	On the first line:
# o	If Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# •	On the following lines, print the matrix.
# Can you re-write the code in case we do not actually move Alices position, just imagine and calculate, but mark with "*" every commanded move

rows_count = int(input())
matrix = [list(input().split()) for _ in range(rows_count)]
tea_bags = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
alice_first_position = [[i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "A"][0]

def print_matrix():
    for row in matrix:
        print(*row, sep=" ")


command = input()

while command:
    alice_new_position = [alice_first_position[0] + directions[command][0], alice_first_position[1] + directions[command][1]]
    if 0 <= alice_new_position[0] < rows_count and 0 <= alice_new_position[1] < rows_count:
        if matrix[alice_new_position[0]][alice_new_position[1]] == "R":
            matrix[alice_first_position[0]][alice_first_position[1]] = "*"
            print("Alice didn't make it to the tea party.")
            print_matrix()
            break
        elif matrix[alice_new_position[0]][alice_new_position[1]].isdigit():
            tea_bags += int(matrix[alice_new_position[0]][alice_new_position[1]])
            matrix[alice_first_position[0]][alice_first_position[1]] = "*"
            matrix[alice_new_position[0]][alice_new_position[1]] = "A"
            alice_first_position = alice_new_position
        elif matrix[alice_new_position[0]][alice_new_position[1]] == ".":
            matrix[alice_first_position[0]][alice_first_position[1]] = "*"
            matrix[alice_new_position[0]][alice_new_position[1]] = "A"
            alice_first_position = alice_new_position
    else:
        matrix[alice_first_position[0]][alice_first_position[1]] = "*"
        print("Alice didn't make it to the tea party.")
        print_matrix()
        break
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        print_matrix()
        break
    command = input()








# def print_matrix():
#     for row in matrix:
#         print(*row, sep=" ")


# def is_valid_position(i, j):
#     return 0 <= i < rows_count and 0 <= j < rows_count


# def get_new_position(i, j, command):
#     new_i = i + directions[command][0]
#     new_j = j + directions[command][1]
#     return new_i, new_j


# def is_rabbit_hole(i, j):
#     return matrix[i][j] == "R"


# def is_empty_position(i, j):
#     return matrix[i][j] == "."


# def is_tea_bag(i, j):
#     return matrix[i][j].isdigit()


# def collect_tea(i, j):
#     global colected_tea
#     colected_tea += int(matrix[i][j])
#     return colected_tea


# def is_end_of_game():
#     return colected_tea >= 10


# def is_out_of_territory(i, j):
#     return not is_valid_position(i, j)


# def is_alice_position(i, j):
#     return matrix[i][j] == "A"


# def remove_old_position(i, j):
#     matrix[i][j] = "*"  # remove old position
#     return matrix


# def update_alice_position(i, j):
#     matrix[i][j] = "A"
#     return matrix


# def move_alice(i, j, command):
#     new_i, new_j = get_new_position(i, j, command)
#     if is_out_of_territory(new_i, new_j):
#         remove_old_position(i, j)
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif is_rabbit_hole(new_i, new_j):
#         remove_old_position(i, j)
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif is_empty_position(new_i, new_j):
#         remove_old_position(i, j)
#         update_alice_position(new_i, new_j)
#     elif is_tea_bag(new_i, new_j):
#         collect_tea(new_i, new_j)
#         remove_old_position(i, j)
#         update_alice_position(new_i, new_j)
#     return matrix


# def find_alice_position():
#     for i, row in enumerate(matrix):
#         for j, item in enumerate(row):
#             if item == "A":
#                 return i, j
#     return None


# def play_game():
#     while True:
#         try:
#             command = input()
#         except EOFError:
#             print("Alice didn't make it to the tea party.")
#             print_matrix()
#             exit()
#         i, j = find_alice_position()
#         move_alice(i, j, command)
#         if is_end_of_game():
#             print("She did it! She went to the party.")
#             print_matrix()
#             exit()


# def main():
#     play_game()


# if __name__ == "__main__":
#     main()

# while colected_tea < 10:
#     command = input()
#     # if on the new alice position is "*" or "R" or out of the matrix, print and exit
#     if matrix[alice_position[0]][alice_position[1]].isdigit():
#         colected_tea += int(matrix[alice_position[0]][alice_position[1]])
#     else:
#         matrix[alice_position[0]][alice_position[1]] = "*"  # remove old position

#     for i, row in enumerate(matrix):
#         for j, item in enumerate(row):
#             if item == "A":
#                 alice_position = (i, j)
#                 # remove old position
#                 matrix[alice_position[0]][alice_position[1]] = "*"  # remove old position
#                 break
#         else:
#             continue
#         break
#     new_i = alice_position[0] + directions[command][0]
#     new_j = alice_position[1] + directions[command][1]
#     # if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#     if not (0 <= new_i < rows_count and 0 <= new_j < rows_count):
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == "R":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == ".":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         matrix[new_i][new_j] = "A"
#         alice_position = [new_i, new_j]
#     else:
#         if matrix[new_i][new_j].isdigit():
#             colected_tea += int(matrix[new_i][new_j])
#             matrix[alice_position[0]][alice_position[1]] = "*"
#             matrix[new_i][new_j] = "A"
#             alice_position = [new_i, new_j]
#     if command == "up" and new_i < 0:
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()

# matrix[alice_position[0]][alice_position[1]] = "*"  # remove old position
# print("She did it! She went to the party.")
# print_matrix()


# rows_count = int(input())
# matrix = [[x for x in input().split()] for _ in range(rows_count)]
# colected_tea = 0
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


# def print_matrix():
#     for row in matrix:
#         print(*row, sep=" ")


# while colected_tea < 10:
#     command = input()
#     # update alice position, check if it is valid and remove the old position
#     # alice_position = next(((i, j) for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "A"), None)
#     alice_position = next(
#         (
#             (i, j)
#             for i in range(rows_count)
#             for j in range(rows_count)
#             if matrix[i][j] == "A"
#         ),
#         None,
#     )
#     if alice_position is None:
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     else:
#         matrix[alice_position[0]][alice_position[1]] = "*"  # remove old position
#     new_i = alice_position[0] + directions[command][0]
#     new_j = alice_position[1] + directions[command][1]
#     if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == "R":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == ".":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         matrix[new_i][new_j] = "A"
#         alice_position = [new_i, new_j]
#     else:
#         if matrix[new_i][new_j].isdigit():
#             colected_tea += int(matrix[new_i][new_j])
#             matrix[alice_position[0]][alice_position[1]] = "*"
#             matrix[new_i][new_j] = "A"
#             alice_position = [new_i, new_j]

# # replace alice position with *
# alice_position = matrix[alice_position[0]][
#     alice_position[1]
# ] = "*"  # remove old position

# print("She did it! She went to the party.")
# print_matrix()


# rows_count = int(input())
# matrix = [[x for x in input().split()] for _ in range(rows_count)]
# colected_tea = 0
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
# alice_position = [ [i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "A"][0]

# def print_matrix():
#     for row in matrix:
#         print(*row, sep=" ")

# while colected_tea < 10:
#     command = input()
#     new_i = alice_position[0] + directions[command][0]
#     new_j = alice_position[1] + directions[command][1]
#     if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == "R":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         print("Alice didn't make it to the tea party.")
#         print_matrix()
#         exit()
#     elif matrix[new_i][new_j] == ".":
#         matrix[alice_position[0]][alice_position[1]] = "*"
#         matrix[new_i][new_j] = "A"
#         alice_position = [new_i, new_j]
#     else:
#         if matrix[new_i][new_j].isdigit():
#             colected_tea += int(matrix[new_i][new_j])
#             matrix[alice_position[0]][alice_position[1]] = "*"
#             matrix[new_i][new_j] = "A"
#             alice_position = [new_i, new_j]

# print("She did it! She went to the party.")
# print_matrix()


# rows_count = int(input())
# matrix = [[x for x in input().split()] for _ in range(rows_count)]
# colected_tea = 0
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
# colected_commands = [command for command in input().split()]

# for command in colected_commands:
#     if colected_tea >= 10:
#         break
#     for i in range(rows_count):
#         for j in range(rows_count):
#             if matrix[i][j] == "A":
#                 matrix[i][j] = "*"
#                 new_i = i + directions[command][0]
#                 new_j = j + directions[command][1]
#                 if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == "R":
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == ".":
#                     matrix[new_i][new_j] = "A"
#                 else:
#                     if matrix[new_i][new_j].isdigit():
#                         colected_tea += int(matrix[new_i][new_j])
#                         matrix[new_i][new_j] = "A"
#                 break
#         else:
#             continue
#         break

# print("She did it! She went to the party.")
# for row in matrix:
#     print(*row, sep=" ")


# for i in range(rows_count):
#     for j in range(rows_count):
#         if matrix[i][j] == "A":
#             while colected_tea < 10:
#                 command = input()
#                 new_i = i + directions[command][0]
#                 new_j = j + directions[command][1]
#                 if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#                     matrix[i][j] = "*"
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == "R":
#                     matrix[i][j] = "*"
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == ".":
#                     matrix[i][j] = "*"
#                     matrix[new_i][new_j] = "A"
#                     i, j = new_i, new_j
#                 else:
#                     if matrix[new_i][new_j].isdigit():
#                         colected_tea += int(matrix[new_i][new_j])
#                         matrix[i][j] = "*"
#                         matrix[new_i][new_j] = "A"
#                         i, j = new_i, new_j
#             break
#     else:
#         continue
#     break

# print("She did it! She went to the party.")
# for row in matrix:
#     print(*row, sep=" ")


# rows_count = int(input())
# matrix = [[x for x in input().split()] for _ in range(rows_count)]
# colected_tea = 0
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


# while colected_tea < 10:
#     for i in range(rows_count):
#         for j in range(rows_count):
#             if matrix[i][j] == "A":
#                 command = input()
#                 matrix[i][j] = "*"
#                 new_i = i + directions[command][0]
#                 new_j = j + directions[command][1]
#                 if new_i < 0 or new_i >= rows_count or new_j < 0 or new_j >= rows_count:
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == "R":
#                     print("Alice didn't make it to the tea party.")
#                     for row in matrix:
#                         print(*row, sep=" ")
#                     exit()
#                 elif matrix[new_i][new_j] == ".":
#                     matrix[new_i][new_j] = "A"
#                 else:
#                     if matrix[new_i][new_j].isdigit():
#                         colected_tea += int(matrix[new_i][new_j])
#                         matrix[new_i][new_j] = "A"
#                 break
#         else:
#             continue
#         break

# # swap the last position with "A" with "*"
# for i in range(rows_count):
#     for j in range(rows_count):
#         if matrix[i][j] == "A":
#             matrix[i][j] = "*"

# print("She did it! She went to the party.")

# for row in matrix:
#     print(*row, sep=" ")
