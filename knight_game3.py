# Knight Game
# Chess is the oldest game, but it is still popular these days.
# It will be used only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally,
# then one square vertically, or it can move one square horizontally, then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with a "K" for knights and a "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"
# Output
# •	Print a single integer with the number of knights that need to be removed.


rows_count = int(input())
matrix = [[x for x in input()] for _ in range(rows_count)]
all_knights = [[i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "K"]
all_knights_count = len(all_knights)
removed_knights = 0
knight_moves = {(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)}

while True:
    max_knights = 0
    max_knight = []
    for knight in all_knights:
        current_knights = 0
        if knight[0] > 1 and knight[1] > 1 and knight[0] < rows_count - 2 and knight[1] < rows_count - 2:
            for move in knight_moves:
                if matrix[knight[0]+move[0]][knight[1]+move[1]] == "K":
                    current_knights += 1
            if current_knights > max_knights:
                max_knights = current_knights
                max_knight = knight
    if max_knights == 0:
        break
    else:
        matrix[max_knight[0]][max_knight[1]] = "0"
        removed_knights += 1
        all_knights.remove(max_knight)
print(removed_knights)

# rows_count = int(input())
# matrix = [[x for x in input()] for _ in range(rows_count)]
# all_knights = [[i, j] for i in range(rows_count) for j in range(rows_count) if matrix[i][j] == "K"]
# all_knights_count = len(all_knights)
# removed_knights = 0
# knight_moves = {(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)}

# for knight in all_knights:
#     if knight[0] > 1 and knight[1] > 1 and knight[0] < rows_count - 2 and knight[1] < rows_count - 2:
#         for move in knight_moves:
#             if matrix[knight[0]+move[0]][knight[1]+move[1]] == "K":
#                 if not [knight[0]+move[0],knight[1]+move[1]] in all_knights:
#                     continue
#                 matrix[knight[0]][knight[1]] = "0"
#                 removed_knights = removed_knights + 1
#                 all_knights.remove([knight[0]+move[0],knight[1]+move[1]])
#                 break
# print(removed_knights)

# for knight in all_knights:
#     if knight[0] > 1 and knight[1] > 1 and knight[0] < rows_count - 2 and knight[1] < rows_count - 2:
#         for move in knight_moves:
#             if matrix[knight[0]+move[0]][knight[1]+move[1]] == "K":
#                 matrix[knight[0]][knight[1]] = "0"
#                 removed_knights += 1
#                 break
# print(removed_knights)


# while True:
#     max_knights = 0
#     max_knight = []
#     for knight in all_knights:
#         current_knights = 0
#         if knight[0] > 1 and knight[1] > 1 and knight[0] < rows_count - 2 and knight[1] < rows_count - 2:
#             if matrix[knight[0] - 2][knight[1] - 1] == "K":
#                 current_knights += 1
#             if matrix[knight[0] - 2][knight[1] + 1] == "K":
#                 current_knights += 1
#             if matrix[knight[0] - 1][knight[1] - 2] == "K":
#                 current_knights += 1
#             if matrix[knight[0] - 1][knight[1] + 2] == "K":
#                 current_knights += 1
#             if matrix[knight[0] + 1][knight[1] - 2] == "K":
#                 current_knights += 1
#             if matrix[knight[0] + 1][knight[1] + 2] == "K":
#                 current_knights += 1
#             if matrix[knight[0] + 2][knight[1] - 1] == "K":
#                 current_knights += 1
#             if matrix[knight[0] + 2][knight[1] + 1] == "K":
#                 current_knights += 1
#         if current_knights > max_knights:
#             max_knights = current_knights
#             max_knight = knight
#     if max_knights == 0:
#         break
#     else:
#         matrix[max_knight[0]][max_knight[1]] = "0"
#         removed_knight += 1
#         all_knights.remove(max_knight)

# print(removed_knight)


# for i in range(rows_count):
#     for j in range(rows_count):
#         if matrix[i][j] == "K":
#             if i > 1 and j > 1 and i < rows_count - 2 and j < rows_count - 2:
#                     matrix[i - 2][j - 1] == "K"
#                     or matrix[i - 2][j + 1] == "K"
#                     or matrix[i - 1][j - 2] == "K"
#                     or matrix[i - 1][j + 2] == "K"
#                     or matrix[i + 1][j - 2] == "K"
#                     or matrix[i + 1][j + 2] == "K"
#                     or matrix[i + 2][j - 1] == "K"
#                     or matrix[i + 2][j + 1] == "K"
#                 ):
#                     removed_knights += 1

# print(removed_knights)


# rows_count = int(input())
# matrix = [[x for x in input()] for _ in range(rows_count)]
# knight_to_remove = 0

# for i in range(rows_count):
#     for j in range(rows_count):
#         if matrix[i][j] == "K":
#             if i > 1 and j > 1 and i < rows_count - 2 and j < rows_count - 2:
#                 if (
#                     matrix[i - 2][j - 1] == "K"
#                     or matrix[i - 2][j + 1] == "K"
#                     or matrix[i - 1][j - 2] == "K"
#                     or matrix[i - 1][j + 2] == "K"
#                     or matrix[i + 1][j - 2] == "K"
#                     or matrix[i + 1][j + 2] == "K"
#                     or matrix[i + 2][j - 1] == "K"
#                     or matrix[i + 2][j + 1] == "K"
#                 ):
#                     knight_to_remove += 1

# print(knight_to_remove)

# while True:
#     max_sum = { "sum": 0, "row": 0, "col": 0 }
#     for i in range(rows_count):
#         for j in range(rows_count):
#             if matrix[i][j] == "K" and i > 1 and j > 1 and i < rows_count - 2 and j < rows_count - 2:
#                 current_sum = sum(
#                     [
#                         1 if matrix[i - 2][j - 1] == "K" else 0,
#                         1 if matrix[i - 2][j + 1] == "K" else 0,
#                         1 if matrix[i - 1][j - 2] == "K" else 0,
#                         1 if matrix[i - 1][j + 2] == "K" else 0,
#                         1 if matrix[i + 1][j - 2] == "K" else 0,
#                         1 if matrix[i + 1][j + 2] == "K" else 0,
#                         1 if matrix[i + 2][j - 1] == "K" else 0,
#                         1 if matrix[i + 2][j + 1] == "K" else 0,
#                     ]
#                 )
#                 if current_sum > max_sum["sum"]:
#                     max_sum["sum"] = current_sum
#                     max_sum["row"] = i
#                     max_sum["col"] = j
#     if max_sum["sum"] == 0:
#         break
#     matrix[max_sum["row"]][max_sum["col"]] = "0"

# print(sum([sum([1 if x == "K" else 0 for x in row]) for row in matrix]))

# print(sum([sum([1 if x == "K" else 0 for x in row]) for row in matrix]))
# print(sum([row.count("K") for row in matrix]))
# print sum of all "K" that need to be removed
