# Maximal Sum
# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. 
# There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
# •	On the following lines, you will receive each row with its columns - integers, 
# separated by a single space in the range [-20, 20]
# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a single space

rows_count, columns_count = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]
max_sum = [[sum([matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2] for j in range(columns_count - 2)]) for i in range(rows_count - 2)]]
print(f"Sum = {max([max(x) for x in max_sum])}")
print(*[matrix[i][j:j + 3] for i in range(rows_count - 2) for j in range(columns_count - 2) if sum([matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2] for j in range(columns_count - 2)]) == max([max(x) for x in max_sum])][0], sep = " ")