# The Squirrel
 
# An intern from a big company must solve the game - "The squirrel". He doesn’t have enough experience, so he needs your help.
# Here are the rules of the game:
# The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
# You get as input the size of the field, which will be always a square shape. After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up" in a sequence, each value separated by a comma and a space (", "). On the next rows, you will receive the field.
# Possible characters in the field:
# •	s - represents the squirrel's position.
# •	h – represents a hazelnut. 
# •	* – the asterisk represents an empty position.
# •	t – represents a trap.
# The squirrel starts from the s - position.
# •	If the squirrel steps on a hazelnut, you have to increase them by 1. The position should be marked with an asterisk (*).
# o	If the squirrel collects all 3 hazelnuts, the game ends.
# •	Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
# •	If it steps on a trap, the game ends.
# •	If the squirrel moves out of the field, the game ends.
# After all commands you will have 4 possible results:
# •	You win if the squirrel collects 3 of the hazelnuts.
# •	The squirrel collects less than 3 hazelnuts.
# •	The squirrel steps on a trap.
# •	The squirrel moves out of the field.
# Input
# •	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
# •	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
# •	In the next N lines, you will receive the values for every row.
# Output
# •	On the first line:
# o	If the squirrel goes out of the field - "The squirrel is out of the field.".
# o	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
# o	If the squirrel hasn’t collected all hazelnuts - "There are more hazelnuts to collect.".
# o	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
# •	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
# Constraints
# •	The input will always be valid.
# •	There will always be a squirrel on the field.
# •	There will always be at least 1 hazelnut on the field.



def main():
    size_of_field = int(input())
    directions = input().split(', ')
    field = [list(input()) for _ in range(size_of_field)]

    squirrel_row, squirrel_col = find_squirrel_position(field)

    hazelnuts_collected = 0

    for direction in directions:
        new_row, new_col = move(squirrel_row, squirrel_col, direction)

        if not is_inside(new_row, new_col, size_of_field):
            print("The squirrel is out of the field.")
            break

        if field[new_row][new_col] == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        if field[new_row][new_col] == 'h':
            hazelnuts_collected += 1
            if hazelnuts_collected == 3:
                print("Good job! You have collected all hazelnuts!")
                break

        field[squirrel_row][squirrel_col] = '*'
        squirrel_row, squirrel_col = new_row, new_col

    else:
        print("There are more hazelnuts to collect.")

    print(f"Hazelnuts collected: {hazelnuts_collected}")


def find_squirrel_position(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == 's':
                return row, col


def move(row, col, direction):
    if direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1
    elif direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


if __name__ == "__main__":
    main()