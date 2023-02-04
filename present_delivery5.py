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


def eat_cookie(presents_left, nice_kids):  # създаваме фунцкия, първи параметър останалите подаръци и втори добрите деца
    for x, y in directions.values():  # обхождаме всяка посока от посоките
        r = santa_pos[0] + x  # намираме реда като съберем реда на Дядо Коледа и реда от посоката
        c = santa_pos[1] + y  # намираме колоната като съберем колоната на Дядо Коледа и тази от посоката

        if neighborhood[r][c].isalpha():  # проверяваме дали сме стъпили на буква
            if neighborhood[r][c] == 'V':  # проверяваме дали сме в къщата на добро дете
                nice_kids += 1  # увеличаваме броя на посетените добри деца за скоупа на функцията

            neighborhood[r][c] = '-'  # заменяме позицията, на която сме с тире
            presents_left -= 1  # намаляме наличните подаръци с 1, в скоупа на функцията

        if not presents_left:  # проверяваме дали са ни свършили подаръците
            break  # прекратяваме цикъла

    return presents_left, nice_kids  # връщаме наличните подаръци и броя на посетените добри деца


presents = int(input())  # прочитаме броя подаръци
size = int(input())  # прочитаме размера на матрицата

neighborhood = []  # създаваме променлива, в която да пазим матрицата
santa_pos = []  # създаваме променлива, в която да пазим позицията на Дядо Коледа

total_nice_kids = 0  # създаваме променлива, в която да пазим броя на добрите деца
nice_kids_visited = 0  # създаваме променлива, в която да пазим броя на посетените добри деца

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
    line = input().split()  # прочитаме ред от конзолата и го разделяме по спейс

    neighborhood.append(line)  # добавяме реда към матрицата

    if 'S' in line:  # проверяваме дали Дядо Коледа е на този ред
        santa_pos = [row, line.index('S')]  # запазваме позицията на Дядо Коледа
        neighborhood[row][santa_pos[1]] = '-'  # променяме стойността на позицията на Дядо Коледа на тире

    total_nice_kids += line.count('V')  # добавяме броя им от реда, към общия брой добри деца

command = input()  # прочитаме команда, опции - up, down, left, right, Christmas morning

while command != "Christmas morning":  # развъртаме while цикъл, докато командата е различна от Christmas morning
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]  # обновяваме позицията на Дядо Коледа, като събираме текущата му позиция с тази от координатите

    house = neighborhood[santa_pos[0]][santa_pos[1]]  # запазваме стойността на текущата къща

    if house == 'V':  # проверяваме дали в къщата има добро дете
        nice_kids_visited += 1  # увеличаваме броя на посетените добри деца
        presents -= 1  # намаляме броя на подаръците
    elif house == 'C':  # проверяваме дали в къщата има бисквитки
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)  # извикваме функцията eat_cookies()

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'  # заменяме позицията, на която сме с тире

    if not presents or nice_kids_visited == total_nice_kids:
        break  # проверяваме дали са ни свършили подаръците или сме минали през всички добри деца в квартала

    command = input()  # прочитаме команда

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'  # поставяме Дядо Коледа на позицията му

if not presents and nice_kids_visited < total_nice_kids:  # проверка нямаме подаръци и не сме посетили всички добри деца
    print('Santa ran out of presents!')  # принтираме, Santa ran out of presents!

print(*[' '.join(line) for line in neighborhood], sep='\n')  # принтираме матрицата, като джойнваме всеки ред по спейс

if nice_kids_visited == total_nice_kids:  # проверяваме дали всички добри деца са получили подаръци
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')  # принтираме
else:  # ако не всички добри деца са получили подаръци
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')  # принтирамеid/s.")
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
