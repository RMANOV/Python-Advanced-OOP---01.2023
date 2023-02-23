# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n.

def rhombus_of_stars(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)

n = int(input())
rhombus_of_stars(n)