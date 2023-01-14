# Primary Diagonal
# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
# On the first line, you will receive an integer N – the size of a square matrix. 
# The next N lines holds the values for each column - N numbers, separated by a single space.

rows_count = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]
primary_diagonal = [matrix[i][i] for i in range(rows_count)]
print(sum(primary_diagonal))
