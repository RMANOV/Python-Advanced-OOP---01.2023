# Sum Matrix Elements
# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

rows, columns = [int(x) for x in input().split(", ")]
sum_matrix = 0

for row in range(rows):
    matrix = [int(x) for x in input().split(", ")]
    sum_matrix += sum(matrix)
    print(matrix)


print(sum_matrix)