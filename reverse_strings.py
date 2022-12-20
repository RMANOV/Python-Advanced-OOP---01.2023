

# Write a program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console
# using the stack data structure

initial_list = list(input())

for i in range(len(initial_list)):
    print(initial_list.pop(), end="")
