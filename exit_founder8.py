# Read the input
first_player, second_player = input().split(", ")
matrix = [input().split() for _ in range(6)]

# Set the initial positions of the players to outside the board
first_player_position = [-1, -1]
second_player_position = [-1, -1]

# Find the positions of the players in the matrix
for i in range(6):
    for j in range(6):
        if matrix[i][j] == "T":
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
        matrix[current_position[0]][current_position[1]] = (
            "T" if current_player == first_player else "J"
        )

    # Update the positions of the players in the matrix
    if current_player == first_player:
        first_player_position = current_position
        second_player_position = opponent_position
    else:
        second_player_position = current_position
        first_player_position = opponent_position

    # Switch to the other player
    current_player, opponent = opponent, current_player
