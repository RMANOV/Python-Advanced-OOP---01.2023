# Symbol in Matrix
# Write a program that reads a number - N, representing the rows and columns of a square matrix. 
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. 
# After that, you will receive a symbol. 
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". 
# You should start searching from the top left. 
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".

rows_count = int(input())
matrix = [[x for x in input()] for _ in range(rows_count)]
symbol = input()
symbols_coordinates = []

for row_index in range(rows_count):
    for col_index in range(rows_count):
        if matrix[row_index][col_index] == symbol:
            symbols_coordinates.append(row_index)
            symbols_coordinates.append(col_index)
            break
    if symbols_coordinates:
        break
print(f"({symbols_coordinates[0]}, {symbols_coordinates[1]})" if symbols_coordinates else f"{symbol} does not occur in the matrix")

# symbols_coordinates = [x for x in range(rows_count) for y in range(rows_count) if matrix[x][y] == symbol]
# print(f"({symbols_coordinates[-2]}, {symbols_coordinates[-1]})" if symbols_coordinates else f"{symbol} does not occur in the matrix")


# if len(symbols_coordinates) == 2:
#     print(f"({symbols_coordinates[0]}, {symbols_coordinates[1]})")
# else:
#     print(f"{symbol} does not occur in the matrix")
