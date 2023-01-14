# Sum Matrix Columns
# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
# On the first line, you will get matrix sizes in format "{rows}, {columns}". 
# On the next rows, you will get elements for each column separated with a single space. 

rows_count, columns_count = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]

for column in range(columns_count):
    column_sum = 0
    for row in range(rows_count):
        column_sum += matrix[row][column]
    print(column_sum)

