# Blind Man’s Buff
# Blind man's buff is played in a spacious area, such as outdoors or in a large room,
# in which one player, is blindfolded and gropes around attempting to touch the other players without being able to see them…
# You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines,
# you will receive the rows of the playground, with M columns. You will be marked with the letter 'B',
# and placed in a random position. In random positions, furniture or other obstacles will be marked with the letter 'O'.
# The other players (opponents) will be marked with the letter 'P'. There will always be three other players participating in the game.
# All of the empty positions will be marked with '-'.
# Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an obstacle.
# On the next few lines, until you receive the command "Finish",
# you will receive a few lines with commands representing which direction you need to move.
# The possible directions are "up", " down", "right", and "left". If the direction leads you out of the field,
# you need to stay in position inside the field(do NOT make the move). If you have an obstacle, towards the direction,
# do NOT make the move and wait for the next command.
# You need to keep track of the count of touched opponents and the moves you’ve made.
# In case you step on a position marked with '-', increase the count of the moves made.
# When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
# If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents and moves made),
# and this is your new position.
# The game is over when you manage to touch all other opponents or the given command is "Finish". A game report is printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"

# Input
# •	On the first line, you'll receive the dimensions of the playground in the format: "N M",
# where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
# •	On the next N lines, you will receive a string representing the respective row of the playground.
# The positions in every string will be separated by a single space (" ").
# •	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).
#
# Output
# •	When the game is over, the following output should be printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"
# Constraints
# •	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
# •	The playground will always have three opponents in it - 'P'.
# •	The obstacles on the playground will always be random count, and there will be cases without any obstacles.

n, m = map(int, input().split())
playground = [input().split() for _ in range(n)]
moves_made = 0
touched_opponents = 0
x, y = None, None

for i in range(n):
    for j in range(m):
        if playground[i][j] == 'B':
            x, y = i, j

while True:
    direction = input()
    new_x, new_y = x, y

    if direction == 'up':
        new_x -= 1
    elif direction == 'down':
        new_x += 1
    elif direction == 'left':
        new_y -= 1
    elif direction == 'right':
        new_y += 1

    if 0 <= new_x < n and 0 <= new_y < m:
        if playground[new_x][new_y] == '-':
            moves_made += 1
            x, y = new_x, new_y
        elif playground[new_x][new_y] == 'P':
            moves_made += 1
            touched_opponents += 1
            playground[new_x][new_y] = '-'
            x, y = new_x, new_y

        if touched_opponents == 3:
            print("Game over!")
            print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
            break
    else:
        continue

    if direction == 'Finish':
        print("Game over!")
        print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
        break
