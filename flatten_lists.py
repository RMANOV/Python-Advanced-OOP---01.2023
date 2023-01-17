# Flatten Lists
# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right, as shown below.

initial_string = input()

sublist = []

for i in initial_string.split("|"):
    sublist.append(i.split())
sublist.reverse()

print(" ".join([j for i in sublist for j in i]))
