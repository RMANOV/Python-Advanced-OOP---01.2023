# Easter Bunny
# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with the symbol "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction.
# For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected

rows_count = int(input())
matrix = [[x for x in input().split()] for _ in range(rows_count)]
bunny_movings = {(-1, 0), (1, 0), (0, -1), (0, 1)}
bunny_position = [ [i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "B" ]
max_collected_eggs = 0
max_collected_eggs_direction = ""
max_collected_eggs_indexes = []

for move in bunny_movings:
    collected_eggs = 0
    collected_eggs_indexes = []
    current_position = [bunny_position[0][0], bunny_position[0][1]]
    while True:
        if (
            current_position[0] + move[0] >= 0
            and current_position[0] + move[0] < rows_count
            and current_position[1] + move[1] >= 0
            and current_position[1] + move[1] < rows_count
        ):
            if matrix[current_position[0] + move[0]][current_position[1] + move[1]] != "X":
                if matrix[current_position[0] + move[0]][current_position[1] + move[1]] != "B":
                    collected_eggs += int(matrix[current_position[0] + move[0]][current_position[1] + move[1]])
                    collected_eggs_indexes.append([current_position[0] + move[0], current_position[1] + move[1]])
                    current_position = [current_position[0] + move[0], current_position[1] + move[1]]
                else:
                    break
            else:
                break
        else:
            break
    if collected_eggs > max_collected_eggs:
        max_collected_eggs = collected_eggs
        max_collected_eggs_direction = move
        max_collected_eggs_indexes = collected_eggs_indexes



# print up, down, left, right if max_collected_egg is apropriate
for move in bunny_movings:
    if move == max_collected_eggs_direction:
        if move == (-1, 0):
            print("up")
        elif move == (1, 0):
            print("down")
        elif move == (0, -1):
            print("left")
        elif move == (0, 1):
            print("right")


print(*max_collected_eggs_indexes, sep="\n")
print(max_collected_eggs)

# for i in range(rows_count):
#     for j in range(rows_count):
#         if matrix[i][j] == "B":
#             bunny_position.append([i, j])

# while True:
#     max_collected_eggs = 0
#     max_collected_eggs_direction = ""
#     max_collected_eggs_indexes = []
#     for move in bunny_movings:
#         collected_eggs = 0
#         collected_eggs_indexes = []
#         current_position = [bunny_position[0][0], bunny_position[0][1]]
#         while True:
#             if (
#                 current_position[0] + move[0] >= 0
#                 and current_position[0] + move[0] < rows_count
#                 and current_position[1] + move[1] >= 0
#                 and current_position[1] + move[1] < rows_count
#             ):
#                 if matrix[current_position[0] + move[0]][current_position[1] + move[1]] != "X":
#                     if matrix[current_position[0] + move[0]][current_position[1] + move[1]] != "B":
#                         collected_eggs += int(matrix[current_position[0] + move[0]][current_position[1] + move[1]])
#                         collected_eggs_indexes.append([current_position[0] + move[0], current_position[1] + move[1]])
#                         current_position = [current_position[0] + move[0], current_position[1] + move[1]]
#                 else:
#                     break
#             else:
#                 break
#         if collected_eggs > max_collected_eggs:
#             max_collected_eggs = collected_eggs
#             max_collected_eggs_direction = move
#             max_collected_eggs_indexes = collected_eggs_indexes
#     if max_collected_eggs == 0:
#         break
#     else:
#         for index in max_collected_eggs_indexes:
#             matrix[index[0]][index[1]] = "0"
#         bunny_position[0][0] += max_collected_eggs_direction[0]
#         bunny_position[0][1] += max_collected_eggs_direction[1]

# print(max_collected_eggs_direction)
# print(*max_collected_eggs_indexes, sep="\n")
# print(max_collected_eggs)




# rows_count = int(input())
# matrix = [[x for x in input().split()] for _ in range(rows_count)]
# bunny = [
#     [i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "B"
# ][0]
# all_eggs = [
#     int(matrix[i][j])
#     for i in range(rows_count)
#     for j in range(rows_count)
#     if matrix[i][j] != "X" and matrix[i][j] != "B"
# ]

# if sum(all_eggs) <= 0:
#     exit()

# # in wich direction we have the most eggs from the bunny - we sum the eggs in the direction before the trap
# eggs_up = [
#     int(matrix[i][bunny[1]])
#     for i in range(bunny[0] - 1, -1, -1)
#     if matrix[i][bunny[1]] != "X"
# ]
# eggs_up_indexes = [
#     [i, bunny[1]] for i in range(bunny[0] - 1, -1, -1) if matrix[i][bunny[1]] != "X"
# ]

# eggs_down = [
#     int(matrix[i][bunny[1]])
#     for i in range(bunny[0] + 1, rows_count)
#     if matrix[i][bunny[1]] != "X"
# ]
# eggs_down_indexes = [
#     [i, bunny[1]] for i in range(bunny[0] + 1, rows_count) if matrix[i][bunny[1]] != "X"
# ]

# eggs_left = [
#     int(matrix[bunny[0]][i])
#     for i in range(bunny[1] - 1, -1, -1)
#     if matrix[bunny[0]][i] != "X"
# ]
# eggs_left_indexes = [
#     [bunny[0], i] for i in range(bunny[1] - 1, -1, -1) if matrix[bunny[0]][i] != "X"
# ]

# eggs_rigth = [
#     int(matrix[bunny[0]][i])
#     for i in range(bunny[1] + 1, rows_count)
#     if matrix[bunny[0]][i] != "X"
# ]
# eggs_right_indexes = [
#     [bunny[0], i] for i in range(bunny[1] + 1, rows_count) if matrix[bunny[0]][i] != "X"
# ]


# max_eggs = max(sum(eggs_up), sum(eggs_down), sum(eggs_left), sum(eggs_rigth))

# if max_eggs == sum(eggs_up):
#     print("up")
#     print(*eggs_up_indexes, sep="\n")
#     # print(len(eggs_up))
# elif max_eggs == sum(eggs_down):
#     print("down")
#     print(*eggs_down_indexes, sep="\n")
#     # print(len(eggs_down))
# elif max_eggs == sum(eggs_left):
#     print("left")
#     print(*eggs_left_indexes, sep="\n")
#     # print(len(eggs_left))
# elif max_eggs == sum(eggs_rigth):
#     print("right")
#     print(*eggs_right_indexes, sep="\n")
#     # print(len(eggs_rigth))

# print(max_eggs)


# # eggs_up = [[i,j] for i in range(bunny[0]-1,-1,-1) for j in range(rows_count) if matrix[i][j] == "X"]
# # eggs_down = [[i,j] for i in range(bunny[0]+1,rows_count) for j in range(rows_count) if matrix[i][j] == "X"]
# # eggs_left = [[i,j] for i in range(rows_count) for j in range(bunny[1]-1,-1,-1) if matrix[i][j] == "X"]
# # eggs_rigth = [[i,j] for i in range(rows_count) for j in range(bunny[1]+1,rows_count) if matrix[i][j] == "X"]

# eggs_up = []
# for i in range(bunny[0]-1,-1,-1):
#     if matrix[i][bunny[1]] == "X":
#         eggs_up.append([i,bunny[1]])
#     elif matrix[i][bunny[1]] == "X":
#         break
# eggs_down = []
# for i in range(bunny[0]+1,rows_count):
#     if matrix[i][bunny[1]] == "X":
#         eggs_down.append([i,bunny[1]])
#     elif matrix[i][bunny[1]] == "X":
#         break
# eggs_left = []
# for i in range(bunny[1]-1,-1,-1):
#     if matrix[bunny[0]][i] == "X":
#         eggs_left.append([bunny[0],i])
#     elif matrix[bunny[0]][i] == "X":
#         break
# eggs_rigth = []
# for i in range(bunny[1]+1,rows_count):
#     if matrix[bunny[0]][i] == "X":
#         eggs_rigth.append([bunny[0],i])
#     elif matrix[bunny[0]][i] == "X":
#         break

# # in wich direction we have the most eggs
# max_eggs = max(len(eggs_up), len(eggs_down), len(eggs_left), len(eggs_rigth))

# # print the direction
# if max_eggs == len(eggs_up):
#     print("up")
#     print(*eggs_up, sep = "\n")
#     # print(len(eggs_up))
# elif max_eggs == len(eggs_down):
#     print("down")
#     print(*eggs_down, sep = "\n")
#     # print(len(eggs_down))
# elif max_eggs == len(eggs_left):
#     print("left")
#     print(*eggs_left, sep = "\n")
#     # print(len(eggs_left))
# elif max_eggs == len(eggs_rigth):
#     print("right")
#     print(*eggs_rigth, sep = "\n")
#     # print(len(eggs_rigth))
# print(eggs_up + eggs_down + eggs_left + eggs_rigth)


# for i in range(bunny[0]-1,-1,-1):
#     if [i,bunny[1]] in eggs:
#         up.append([i,bunny[1]])
#         up_eggs += 1
#     elif [i,bunny[1]] in traps:
#         break
# for i in range(bunny[0]+1,rows_count):
#     if [i,bunny[1]] in eggs:
#         down.append([i,bunny[1]])
#         down_eggs += 1
#     elif [i,bunny[1]] in traps:
#         break
# for i in range(bunny[1]-1,-1,-1):
#     if [bunny[0],i] in eggs:
#         left.append([bunny[0],i])
#         left_eggs += 1
#     elif [bunny[0],i] in traps:
#         break
# for i in range(bunny[1]+1,rows_count):
#     if [bunny[0],i] in eggs:
#         right.append([bunny[0],i])
#         right_eggs += 1
#     elif [bunny[0],i] in traps:
#         break
# if up_eggs >= down_eggs and up_eggs >= left_eggs and up_eggs >= right_eggs:
#     print("up")
#     print(*up, sep = "\n")
#     # print(up_eggs)
# elif down_eggs >= up_eggs and down_eggs >= left_eggs and down_eggs >= right_eggs:
#     print("down")
#     print(*down, sep = "\n")
#     # print(down_eggs)
# elif left_eggs >= up_eggs and left_eggs >= down_eggs and left_eggs >= right_eggs:
#     print("left")
#     print(*left, sep = "\n")
#     # print(left_eggs)
# elif right_eggs >= up_eggs and right_eggs >= down_eggs and right_eggs >= left_eggs:
#     print("right")
#     print(*right, sep = "\n")
#     # print(right_eggs)
# print(up_eggs + down_eggs + left_eggs + right_eggs)
