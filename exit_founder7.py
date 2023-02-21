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

# 1. Read the input
# 2. Find the positions of the players in the matrix
# 3. Set the initial status of the players
# 4. Set the initial winner
# 5. Set the initial status of the game
# 6. While the game is still going: 
# 7.     Check if the first player needs rest
# 8.     If he doesn't need rest:
# 9.         Get the coordinates of the first player
# 10.        Check if the first player hits the Exit
# 11.        If he hits the Exit:
# 12.            Print the message and end the program
# 13.        Check if the first player hits the Trap
# 14.        If he hits the Trap:
# 15.            Print the message and end the program
# 16.        Check if the first player hits the Wall
# 17.        If he hits the Wall:
# 18.            Print the message and set the status of the first player to "needs rest"
# 19.        Check if the first player is out of the board
# 20.        If he is:
# 21.            Set the winner and end the game
# 22.        Check if both players are in the same position
# 23.        If they are:
# 24.            Set the winner and end the game
# 25.    Check if the second player needs rest
# 26.    If he doesn't need rest:
# 27.        Get the coordinates of the second player
# 28.        Check if the second player hits the Exit
# 29.        If he hits the Exit:
# 30.            Print the message and end the program
# 31.        Check if the second player hits the Trap
# 32.        If he hits the Trap:
# 33.            Print the message and end the program
# 34.        Check if the second player hits the Wall
# 35.        If he hits the Wall:
# 36.            Print the message and set the status of the second player to "needs rest"
# 37.        Check if the second player is out of the board
# 38.        If he is:
# 39.            Set the winner and end the game
# 40.        Check if both players are in the same position
# 41.        If they are:
# 42.            Set the winner and end the game
# 43.    Swap the players
# 44. If the game is over:
# 45.     Print the winner
# 46.     End the program

# Read the input
first_player, second_player = input().split(", ")
matrix = [input().split() for _ in range(6)]

# Set the initial positions of the players to outside the board
player_positions = {first_player: [-1, -1], second_player: [-1, -1]}

# Find the positions of the players in the matrix
for i in range(6):
    for j in range(6):
        if matrix[i][j] == "1":  # "T" or "J"
            player_positions[first_player] = [i, j]
        elif matrix[i][j] == "2":
            player_positions[second_player] = [i, j]

# Set the initial status of the players
# True - needs rest, False - can move - The players start the game with the status "False"
player_status = {first_player: False, second_player: False}

# Set the initial winner
winner = ""

# Set the initial status of the game
# True - the game is still going, False - the game is over
game_status = True

def hiting_wall(player, player_position):
    """Prints the message when a player hits a wall and needs to rest."""
    print(f"{player} hits a wall and needs to rest.")
    player_status[player] = True
    player_positions[player] = player_position
    return True

def is_out_of_board(player_position):
    """Checks if the player is out of the board and sets the winner if he is."""
    global winner, game_status
    if player_position[0] < 0 or player_position[0] > 5 or player_position[1] < 0 or player_position[1] > 5:
        winner = second_player if first_player else first_player
        game_status = False
        return True

def check_if_both_in_same_position():
    """Checks if both players are in the same position and sets the winner if they are."""
    global winner, game_status
    if player_positions[first_player] == player_positions[second_player]:
        winner = second_player if first_player else first_player
        game_status = False
        return True

def check_if_player_hits_exit(player, player_position):
    """Checks if the player hits the Exit and sets the winner if he does."""
    global winner, game_status
    if matrix[player_position[0]][player_position[1]] == "E":
        winner = player
        game_status = False
        return True

def check_if_player_hits_trap(player, player_position):
    """Checks if the player hits the Trap and sets the winner if he does."""
    global winner, game_status
    if matrix[player_position[0]][player_position[1]] == "T":
        winner = second_player if player == first_player else first_player
        game_status = False
        return True



# Read the coordinates of the players
while game_status:
    # Read the coordinates of the first player
    first_player_coordinates = input()
    if not player_status[first_player]:
        row, column = map(
            int, first_player_coordinates.strip("(").strip(")").split(", ")
        )
        is_out_of_board([row, column]) # Check if the player is out of the board
        
        position = matrix[row][column]
        if position == "E":
            check_if_player_hits_exit(first_player, [row, column])
            break
        elif position == "T":
            check_if_player_hits_trap(first_player, [row, column])
            break
        elif position == "W":
            hiting_wall(first_player, [row, column])
        else:
            player_positions[first_player] = [row, column]
            check_if_both_in_same_position()
    else:
        player_status[first_player] = False

    # Read the coordinates of the second player
    second_player_coordinates = input()
    if not player_status[second_player]:
        row, column = map(
            int, second_player_coordinates.strip("(").strip(")").split(", ")
        )
        is_out_of_board([row, column]) # Check if the player is out of the board
        
        position = matrix[row][column]
        if position == "E":
            check_if_player_hits_exit(second_player, [row, column])
            break
        elif position == "T":
            check_if_player_hits_trap(second_player, [row, column])
            break
        elif position == "W":
            hiting_wall(second_player, [row, column])
        else:
            player_positions[second_player] = [row, column]
            check_if_both_in_same_position()
    else:
        player_status[second_player] = False

# Print the result
if winner:
    print(f"{winner} found the Exit and wins the game!")
else:
    print(f"{first_player} is out of the game! The winner is {second_player}.")
