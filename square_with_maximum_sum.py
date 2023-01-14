# Square with Maximum Sum
# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its values. 
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples. 

rows, columns = [int(x) for x in input().split(", ")]
matrix =[[int(x) for x in input().split(", ")] for _ in range(rows)]
max_sum = 0

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = row_index
            max_col_index = col_index

print(f"{matrix[max_row_index][max_col_index]} {matrix[max_row_index][max_col_index + 1]}")
print(f"{matrix[max_row_index + 1][max_col_index]} {matrix[max_row_index + 1][max_col_index + 1]}")
print(max_sum)