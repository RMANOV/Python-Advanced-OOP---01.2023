# Numbers
# First, you will be given two sequences of integers values on different lines. 
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". 
# The values in each sequence should be sorted in ascending order.

first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence.update(map(int, command[2:]))
        elif command[1] == "Second":
            second_sequence.update(map(int, command[2:]))
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence.difference_update(map(int, command[2:]))
        elif command[1] == "Second":
            second_sequence.difference_update(map(int, command[2:]))
    elif command[0] == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

# print(f"{', '.join(map(str, sorted(first_sequence)))} {', '.join(map(str, sorted(second_sequence)))}")

# print(", ".join(map(str, sorted(first_sequence))), end=", ")
# print(", ".join(map(str, sorted(second_sequence))))

# for i in sorted(first_sequence):
#     if i==max(first_sequence):
#         print(i, end="\n")
#     print(i, end=", ")

# print in one line with comma and space - only first sequence
# On new line print second sequence - with comma and space
# print(", ".join(map(str, sorted(first_sequence))), if i==max(first_sequence): print(i, end="\n") print(i, end=", ") print(", ".join(map(str, sorted(second_sequence))))
for i in sorted(first_sequence):
    if i==max(first_sequence):
        print(i, end="\n")
    else:
        print(i, end=", ")
print(", ".join(map(str, sorted(second_sequence))))