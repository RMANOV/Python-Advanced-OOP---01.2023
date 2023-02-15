# Navy Battle
# 1914, September 22 – German submarine U-9 sinks three unescorted British armored cruisers HMS Aboukir,
# HMS Hogue, and HMS Cressy in approximately one hour.
# Imagine that they had the technology to make themselves a navigational program for the submarine and you are chosen to implement the logic.
# Navigate U-9 through the battlefield, find and sink the British cruisers in the dark night, avoiding the floating mines all over the North Sea.
# You will be given an integer n for the size of the battlefield (square shape).
# On the next n lines, you will receive the rows of the battlefield.
# The submarine will start at a random position, marked with the letter 'S'.
# The submarine surveys the surrounding area through its periscope, so it has to climb up to periscope depth,
# where it might run across naval mines.
# When the submarine receives direction, it goes deep and moves one position toward the given direction.
# On each turn, you will be guiding the submarine and giving it the direction, in which it should move.
# The commands will be "up", "down", "left" and "right".
# When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
# •	If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
# •	If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown,
# the position of the mine will be marked with '-' (dash). U-9 can withstand two hits from naval mines.
# The third time the submarine is hit by a mine, it disappears and the mission is failed.
# The battle is over and the following message should be printed on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
# •	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be marked with '-' (dash).
# •	If this is the last (third) battle cruiser on the battlefield,
# the battle is over and the following message should be printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
# The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).
# Input
# •	On the first line, you are given the integer n – the size of the matrix (wall).
# •	The next n lines hold the values for every row (NOT separated by anything).
# •	On each of the next lines you will get a direction command.
# Output
# •	If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
# •	If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!".
# •	At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.

# get the size of the matrix
# get the matrix - row by row - as a list of strings - each string is a row - each row is a list of characters
## separate symbols in each row as a list of characters
# in each row, find the position of the submarine
## check if the submarine is in the row - if not, continue to the next row
## if the submarine is in the row, get the position of the submarine
# get the direction of the submarine
# check if the commands destroy all the battle cruisers or if the submarine is hit by a mine three times
## if the submarine is hit by a mine three times, print the message and break the loop
## if the submarine destroys all the battle cruisers, print the message and break the loop
# if the game is over - break the loop
# concatenate the matrix - row by row - as a list of strings - each string is a row - each row is a list of characters
# print the matrix


# get the size of the matrix
count_of_rows = int(input())
s_row = 0
s_col = 0
matrix = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
number_of_destroyed_cruisers = 0
number_of_hited_mines = 0


# get the matrix - row by row - as a list of strings - each string is a row - each row is a list of characters
for row in range(count_of_rows):
    row = input()
    # separate symbols in each row as a list of characters
    row = list(row)
    # in each row, find the position of the submarine
    if 'S' in row:
        # check if the submarine is in the row - if not, continue to the next row
        # if the submarine is in the row, get the position of the submarine
        s_row = row.index('S')
        s_col = row.index('S')
        # change symbol of the submarine to '-'
        row.remove('S')
        row.insert(s_col, '-')
    # add row to the matrix
    matrix.append(row)


# get the direction of the submarine - after each direction, check if the submarine is hit by a mine or if it destroys a cruiser and replace s with -
while True:
    # get the direction of the submarine
    direction = input()
    # check if the submarine is hit by a mine three times
    if number_of_hited_mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{s_row}, {s_col}]!")
        break
    # check if the submarine destroys all the battle cruisers
    if number_of_destroyed_cruisers == 3:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    # move the submarine
    s_row += directions[direction][0]
    s_col += directions[direction][1]
    # check if the submarine is hit by a mine or if it destroys a cruiser
    if matrix[s_row][s_col] == '*':
        number_of_hited_mines += 1
        matrix[s_row][s_col] = '-'
    elif matrix[s_row][s_col] == 'C':
        number_of_destroyed_cruisers += 1
        matrix[s_row][s_col] = '-'
    # change symbol of the submarine to '-'
    matrix[s_row - directions[direction][0]][s_col - directions[direction][1]] = '-'
    # change symbol of the submarine to 'S'
    matrix[s_row][s_col] = 'S'


# concatenate the matrix - row by row - as a list of strings - each string is a row - each row is a list of characters
# print the matrix
print(*[''.join(row) for row in matrix], sep='\n')
# matrix = [''.join(row) for row in matrix]
