from collections import deque

initial_string = deque(input().split())
colors = []

while len(initial_string) > 1:
    first = initial_string.popleft()
    last = initial_string.pop()
    if first + last in ["red", "yellow", "blue"]:
        colors.append(first + last)
    elif first + last in ["orange", "purple", "green"]:
        if "red" in colors and "yellow" in colors:
            colors.append(first + last)
        else:
            initial_string.insert(int(len(initial_string) / 2), last[:-1])
            initial_string.insert(int(len(initial_string) / 2), first[:-1])
    else:
        initial_string.insert(int(len(initial_string) / 2), last[:-1])
        initial_string.insert(int(len(initial_string) / 2), first[:-1])

if len(initial_string) == 1:
    if initial_string[0] in ["red", "yellow", "blue"]:
        colors.append(initial_string[0])
    elif initial_string[0] in ["orange", "purple", "green"]:
        if "red" in colors and "yellow" in colors:
            colors.append(initial_string[0])
            initial_string.popleft()
    else:
        initial_string.insert(int(len(initial_string) / 2), initial_string[0][:-1])
        initial_string.popleft()

print(colors)
