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

playground = []
for i in range(n):
    row = input().split()
    playground.append(row)

# Find the initial position of the player
for i in range(n):
    for j in range(m):
        if playground[i][j] == "B":
            player_pos = (i, j)
            break

touched_opponents = 0
moves_made = 0
directions = { "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1) }

while True:
    command = input()
    if command == "Finish":
        break

    # Get the direction of the player
    direction = directions[command]

    # Calculate the new position of the player
    new_row = player_pos[0] + direction[0]
    new_col = player_pos[1] + direction[1]

    # Check if the new position is valid
    if 0 <= new_row < n and 0 <= new_col < m:
        # Check if the new position is an obstacle
        if playground[new_row][new_col] == "O":
            continue

        # Check if the new position is an opponent
        if playground[new_row][new_col] == "P":
            touched_opponents += 1

        # Update the playground
        playground[new_row][new_col] = "B"
        playground[player_pos[0]][player_pos[1]] = "-"

        # Update the player position
        player_pos = (new_row, new_col)

    moves_made += 1

    # Check if all opponents are touched
    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
