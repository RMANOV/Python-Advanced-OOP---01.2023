# Sets of Elements
# Write a program that prints a set of elements. 
# On the first line, you will receive two numbers - n and m, separated by a single space - 
# representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers, 
# which are the numbers in the first set, and m numbers, which are in the second set. 
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}

lenght_of_first_set, lenght_of_second_set = input().split()
first_set = set()
second_set = set()
unique_elements = set()

for i in range(int(lenght_of_first_set)):
    first_set.add(input())

for i in range(int(lenght_of_second_set)):
    second_set.add(input())

for element in first_set:
    if element in second_set:
        unique_elements.add(element)

# print(unique_elements) in new lines each element
print(*unique_elements, sep="\n")