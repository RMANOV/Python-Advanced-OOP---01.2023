# 2x2 Squares in Matrix
# Find the number of all 2x2 squares containing identical chars in a matrix. 
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". 
# In the following rows, you will receive characters separated by a single space. 
# Print the number of all square matrices you have found.

rows_count, columns_count = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows_count)]
squares_count = [[matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1] for j in range(columns_count - 1)] for i in range(rows_count - 1)]
print(sum([sum(x) for x in squares_count]))