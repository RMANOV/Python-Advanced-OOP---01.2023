# Diagonal Difference
# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. 
# The following N lines hold the values for each column - N numbers separated by a single space. 
# Print the absolute difference between the primary and the secondary diagonal sums.

rows_count = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_count) ]
primary_diagonal_sum = [matrix[i][i] for i in range(rows_count)]
secondary_diagonal_sum = [matrix[i][rows_count - i - 1] for i in range(rows_count)]

print(abs(sum(primary_diagonal_sum) - sum(secondary_diagonal_sum)))
