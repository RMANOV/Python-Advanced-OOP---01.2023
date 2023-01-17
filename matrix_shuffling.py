# Matrix Shuffling
# Write a program that reads a matrix from the console and performs certain operations with its elements. 
# User input is provided similarly to the problems above - first, you read the dimensions and then the data. 
# Your program should receive commands in the format: 
# "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. 
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step 
# (thus, you will be able to check if the operation was performed correctly). 
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, 
# or the given coordinates are not valid), print "Invalid input!" and move on to the following command. 
# A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

rows_count, columns_count = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows_count)]

while True:
    command = input()
    if command == "END":
        break
    if command.startswith("swap") and len(command.split()) == 5:
        command = command.split()
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if row1 in range(rows_count) and row2 in range(rows_count) and col1 in range(columns_count) and col2 in range(columns_count):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for i in range(rows_count):
                print(*matrix[i], sep=" ")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")


