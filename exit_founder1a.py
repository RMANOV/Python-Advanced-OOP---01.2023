first_player, second_player = input().split(", ")
matrix = [input().split() for _ in range(6)]
first_player_position = [0, 0]
second_player_position = [0, 0]

# Find the starting positions of the players
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == f"{first_player[0]}":
            first_player_position = [row, col]
        elif matrix[row][col] == f"{second_player[0]}":
            second_player_position = [row, col]

# Loop until a player wins or loses
while True:
    # Get the players' next moves
    first_player_coordinates = input()
    second_player_coordinates = input()

    try:
        # Parse the coordinates and ensure they are valid
        first_player_position = [
            int(x) for x in first_player_coordinates[1:-1].split(", ")
        ]
        if not all(0 <= i < 6 for i in first_player_position):
            raise ValueError
        second_player_position = [
            int(x) for x in second_player_coordinates[1:-1].split(", ")
        ]
        if not all(0 <= i < 6 for i in second_player_position):
            raise ValueError
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid coordinates.")
        continue

    # Handle first player's move
    if matrix[first_player_position[0]][first_player_position[1]] == "E":
        print(f"{first_player} found the Exit and wins the game!")
        break
    elif matrix[first_player_position[0]][first_player_position[1]] == "T":
        print(f"{first_player} is out of the game! The winner is {second_player}.")
        break
    elif matrix[first_player_position[0]][first_player_position[1]] == "W":
        print(f"{first_player} hits a wall and needs to rest.")

    # Handle second player's move
    if matrix[second_player_position[0]][second_player_position[1]] == "E":
        print(f"{second_player} found the Exit and wins the game!")
        break
    elif matrix[second_player_position[0]][second_player_position[1]] == "T":
        print(f"{second_player} is out of the game! The winner is {first_player}.")
        break
    elif matrix[second_player_position[0]][second_player_position[1]] == "W":
        print(f"{second_player} hits a wall and needs to rest.")
