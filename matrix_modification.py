# Matrix Modification
# Write a program that reads a matrix from the console and changes its values. 
# On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, 
# separated with a single space. 
# You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". 
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.


# Matrix Modification

# Get matrix size
rows = int(input())

# Create matrix
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    command, row, col, value = command
    row, col, value = int(row), int(col), int(value)
    
    # Check if coordinates are valid
    if not (0 <= row < rows) or not (0 <= col < len(matrix[row])):
        print("Invalid coordinates")
        continue
    
    # Modify matrix values
    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

# Print matrix
for row in matrix:
    print(*row)


# rows_columns = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows_columns[0])]

# while True:
#     command = input()
#     if command == "END":
#         break
#     command, row, col, value = command.split()
#     row, col, value = int(row), int(col), int(value)
#     # if row not in range(rows_columns[0]) or col not in range(rows_columns[1]) or value < 0 or value > 100:
#     if row in range(0, len(matrix)-1) and col in range(0, len(matrix[0])-1):
#         print("Invalid coordinates")
#         continue
#     if command == "Add":
#         matrix[row][col] += value
#     elif command == "Subtract":
#         matrix[row][col] -= value

# print(*[x for x in matrix], sep=" ")


# while True:
#     command = input()
#     if command == "END":
#         break
#     command, row, col, value = command.split()
#     row, col, value = int(row), int(col), int(value)
#     if row not in range(rows_columns[0]) or col not in range(rows_columns[1]):
#         print("Invalid coordinates")
#         continue
#     if command == "Add":
#         matrix[row][col] += value
#     elif command == "Subtract":
#         matrix[row][col] -= value

# print(*[x for x in matrix], sep=" ")
