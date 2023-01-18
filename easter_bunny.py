# Easter Bunny
# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. 
# On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
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
bunny = []
eggs = []
traps = []
for i in range(rows_count):
    for j in range(rows_count):
        if matrix[i][j] == "B":
            bunny = [i,j]
        elif matrix[i][j] == "X":
            traps.append([i,j])
        elif matrix[i][j].isdigit():
            eggs.append([i,j])
up = []
down = []
left = []
right = []
up_eggs = 0
down_eggs = 0
left_eggs = 0
right_eggs = 0

while bunny[0] > 0:
    bunny[0] -= 1
    if [bunny[0],bunny[1]] in eggs:
        up.append([bunny[0],bunny[1]])
        up_eggs += 1
    elif [bunny[0],bunny[1]] in traps:
        break
while bunny[0] < rows_count - 1:
    bunny[0] += 1
    if [bunny[0],bunny[1]] in eggs:
        down.append([bunny[0],bunny[1]])
        down_eggs += 1
    elif [bunny[0],bunny[1]] in traps:
        break
while bunny[1] > 0:
    bunny[1] -= 1
    if [bunny[0],bunny[1]] in eggs:
        left.append([bunny[0],bunny[1]])
        left_eggs += 1
    elif [bunny[0],bunny[1]] in traps:
        break
while bunny[1] < rows_count - 1:
    bunny[1] += 1
    if [bunny[0],bunny[1]] in eggs:
        right.append([bunny[0],bunny[1]])
        right_eggs += 1
    elif [bunny[0],bunny[1]] in traps:
        break
if up_eggs >= down_eggs and up_eggs >= left_eggs and up_eggs >= right_eggs:
    print("up")
    print(*up, sep = "\n")
    # print(up_eggs)
elif down_eggs >= up_eggs and down_eggs >= left_eggs and down_eggs >= right_eggs:
    print("down")
    print(*down, sep = "\n")
    # print(down_eggs)
elif left_eggs >= up_eggs and left_eggs >= down_eggs and left_eggs >= right_eggs:
    print("left")
    print(*left, sep = "\n")
    # print(left_eggs)
elif right_eggs >= up_eggs and right_eggs >= down_eggs and right_eggs >= left_eggs:
    print("right")
    print(*right, sep = "\n")
    # print(right_eggs)

print(up_eggs + down_eggs + left_eggs + right_eggs)


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
