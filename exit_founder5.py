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
player_positions = {first_player: [-1, -1], second_player: [-1, -1]}

# Find the positions of the players in the matrix
for i in range(6):
    for j in range(6):
        if matrix[i][j] == "1":  # "T" or "J"
            player_positions[first_player] = [i, j]
        elif matrix[i][j] == "2":
            player_positions[second_player] = [i, j]

# Find the position of the exit
exit_position = [ [i, j] for i in range(6) for j in range(6) if matrix[i][j] == "E" ][0]

def is_valid_position(position):
    return 0 <= position[0] < 6 and 0 <= position[1] < 6

def switch_player(player):
    return first_player if player == second_player else second_player

def switch_player_position(player):
    return player_positions[second_player] if player == first_player else player_positions[first_player]

def print_result(player, winner):
    print(f"{player} is out of the game! The winner is {winner}.")
    exit()

def print_result_exit(player):
    print(f"{player} found the Exit and wins the game!")
    exit()

def print_result_wall(player):
    print(f"{player} hits a wall and needs to rest.")
    
# Play the game
def play_game():
    current_player = first_player
    while True:
        # Read the coordinates
        row, col = [int(x) for x in input()[1:-1].split(", ")]
        # Check if the coordinates are valid
        if not is_valid_position([row, col]):
            continue
        # Check if the player hits a wall
        if matrix[row][col] == "W":
            print_result_wall(current_player)
            continue
        # Check if the player hits a trap
        if matrix[row][col] == "T":
            print_result(current_player, switch_player(current_player))
        # Check if the player hits the exit
        if matrix[row][col] == "E":
            print_result_exit(current_player)
        # Check if the player steps on the other player
        if player_positions[switch_player(current_player)] == [row, col]:
            print_result(current_player, switch_player(current_player))
        # Update the player's position
        player_positions[current_player] = [row, col]
        # Check if the player has found the exit
        if player_positions[current_player] == exit_position:
            print_result_exit(current_player)
        # Switch the player
        current_player = switch_player(current_player)
        return play_game()

def main():
    play_game()

if __name__ == '__main__':
    main()