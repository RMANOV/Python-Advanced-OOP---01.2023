# Exit Founder
# Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out.
# Monitor their moves closely and find out who the winner will be!
# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ".
# The order in which they are received determines the order in which they will take turns. The first player starts first.
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# •	Only one Exit - marked with the "E" letter
# •	Trap (one, many, or none) - marked with the "T" letter
# •	Wall (one, many, or none) - marked with the "W" letter
# •	Empty positions will be marked with "."
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given,
# you will be receiving coordinates for each of the players.
# They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap.
# Here are the rules:
# •	If a player hits the letter "E", he escapes the maze and wins the game.
# o	Print "{player} found the Exit and wins the game!" and end the program.
# •	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
# o	Print "{player} is out of the game! The winner is {winner}." and end the program.
# •	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
# o	Print "{player} hits a wall and needs to rest."
# •	If a player steps on an empty position ".", nothing happens.
# •	Both players can step in the same position at the same time.
# Input
# •	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
# •	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
# •	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
# Output
# •	You should print the output as described above.
# •	The input coordinates will always be valid.

# Read the input
first_player, second_player = input().split(", ")
matrix = [input().split() for _ in range(6)]

# Set the initial positions of the players to outside the board
first_player_position = [-1, -1]
second_player_position = [-1, -1]

# Find the positions of the players in the matrix
for i in range(6):
    for j in range(6):
        if matrix[i][j] == "1":
            if first_player_position == [-1, -1]:
                first_player_position = [i, j]
            else:
                second_player_position = [i, j]

# Play the game
current_player = first_player
opponent = second_player

while True:
    # Get the current player's position and the opponent's position
    if current_player == first_player:
        current_position = first_player_position
        opponent_position = second_player_position
    else:
        current_position = second_player_position
        opponent_position = first_player_position

    # Get the next move from the current player
    next_move = input().strip()
    next_row, next_col = map(int, next_move[1:-1].split(","))

    # Check if the move is valid
    if not (0 <= next_row < 6 and 0 <= next_col < 6):
        print("Invalid move!")
        continue

    # Update the player's position in the matrix
    if matrix[next_row][next_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
    elif matrix[next_row][next_col] == "T":
        print(f"{current_player} is out of the game! The winner is {opponent}.")
        break
    elif matrix[next_row][next_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    else:
        matrix[current_position[0]][current_position[1]] = "."
        current_position[0], current_position[1] = next_row, next_col
        matrix[current_position[0]][current_position[1]] = str(current_player[0])

    # Switch to the other player
    current_player, first_player_position, second_player_position = (
        second_player,
        second_player_position,
        first_player_position,
    )
