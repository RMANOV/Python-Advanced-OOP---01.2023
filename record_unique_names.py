# Record Unique Names
# Write a program that will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

number_of_names = int(input())
names_set = set()

for i in range(number_of_names):
    name = input()
    names_set.add(name)

unique_names = list(names_set)
unique_names.sort()
for name in unique_names:
    print(name)