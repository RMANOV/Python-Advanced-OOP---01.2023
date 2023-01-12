# Paint Colors
# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. 
# You will be given a string on a single line containing substrings (separated by a single space) 
# from which you will be able to form the following colors: 
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names.
# If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found. 
# When you form a color, remove both substrings. 
# Otherwise, you should remove the last character of each substring and return them in the middle of the original string. 
# If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", 
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
# •	Single line string
# Output
# •	The list with the collected colors

initial_string = input().split()
colors = []

while len(initial_string) > 1:
    first = initial_string[0]
    last = initial_string[-1]
    if first + last in ["red", "yellow", "blue"]:
        colors.append(first + last)
        initial_string.pop(0)
        initial_string.pop(-1)
    elif first + last in ["orange", "purple", "green"]:
        if "red" in initial_string and "yellow" in initial_string:
            colors.append(first + last)
            initial_string.pop(0)
            initial_string.pop(-1)
        else:
            initial_string.insert(int(len(initial_string) / 2), last[:-1])
            initial_string.insert(int(len(initial_string) / 2), first[:-1])
            initial_string.pop(0)
            initial_string.pop(-1)
    else:
        initial_string.insert(int(len(initial_string) / 2), last[:-1])
        initial_string.insert(int(len(initial_string) / 2), first[:-1])
        initial_string.pop(0)
        initial_string.pop(-1)

if len(initial_string) == 1:
    if initial_string[0] in ["red", "yellow", "blue"]:
        colors.append(initial_string[0])
    elif initial_string[0] in ["orange", "purple", "green"]:
        if "red" in initial_string and "yellow" in initial_string:
            colors.append(initial_string[0])
        else:
            initial_string.insert(int(len(initial_string) / 2), initial_string[0][:-1])
            initial_string.pop(0)
    else:
        initial_string.insert(int(len(initial_string) / 2), initial_string[0][:-1])
        initial_string.pop(0)

print(colors)
