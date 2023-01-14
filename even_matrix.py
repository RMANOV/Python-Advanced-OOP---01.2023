# Even Matrix
# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. 
# Use nested comprehension for that problem. 
# On the first line, you will receive the rows of the matrix. On the next rows, 
# you will get elements for each column separated with a comma and a space ", ".

row_count = int(input())

for row in range(row_count):
    matrix = [int(x) for x in input().split(", ")]
    even_matrix = [[x for x in matrix if x % 2 == 0]]
    print(*even_matrix, sep = ", ")
