first_player, second_player = input().split(", ")

maze_board = []

for _ in range(6):
    maze_board.append(input().split())

first_player_needs_rest = False
second_player_needs_rest = False

while True:
    # first player moves
    first_player_coordinates = input()
    if not first_player_needs_rest:
        row, column = map(
            int, first_player_coordinates.strip("(").strip(")").split(", ")
        )
        position = maze_board[row][column]
        if position == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        if position == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if position == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_needs_rest = True
    else:
        first_player_needs_rest = False

    # second_player_moves
    second_player_coordinates = input()
    if not second_player_needs_rest:
        row, column = map(
            int, second_player_coordinates.strip("(").strip(")").split(", ")
        )
        position = maze_board[row][column]
        if position == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        if position == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if position == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False
