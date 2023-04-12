# 01.	Rubber Duck Debuggers

# Rubber Duck Debugging is a type of debugging where you place a rubber duck on your desk and explain to it your code line by line. You gathered a few programmers and gave them a task and judging by the time it took them to write the code, you reward them with a type of rubber ducky.
# Learn more about Rubber Duck Debugging after your exam from here.
# You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a single task. The second one represents the number of tasks you’ve given to your programmers.
# Your task is to count how many rubber ducks of each type you’ve given to your programmers.
# While you have values in the sequences, you need to start from the first value of the programmers time's sequence and multiply them by the last value of the tasks' sequence:
# •	If the calculated time is between any of the time ranges below, you give the corresponding ducky and remove the programmer time's value and the tasks' value.
# •	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2. Then, move the programmer time's value to the end of its sequence, and continue with the next operation.
# Rubber Ducky type	Time needed to earn it
# Darth Vader Ducky	0 - 60
# Thor Ducky	61 – 120
# Big Blue Rubber Ducky	121 - 180
# Small Yellow Rubber Ducky	181 - 240

# Your task is considered done when the sequences are empty.
# Input
# •	The first line will represent each programmer’s time to complete a single task – integers, separated by a single space.
# •	The second line will represent the number of tasks that should be completed – integers, separated by a single space.
# Output
# •	On the first line, you output:
# o	"Congratulations, all tasks have been completed! Rubber ducks rewarded:"
# •	On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
# o	"Darth Vader Ducky: {count}
# Thor Ducky: {count}
# Big Blue Rubber Ducky: {count}
# Small Yellow Rubber Ducky: {count}"

# Constraints
# •	The input will always be valid.
# •	There will always be enough tasks for the programmers.
# •	There will always be enough ducks for the programmers.


from collections import deque

programmers_time = deque([int(x) for x in input().split()]) 
tasks = deque([int(x) for x in input().split()])

ducky = { "Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0 }

while programmers_time and tasks:
    time = programmers_time[0] * tasks[-1]
    if time <= 60:
        ducky["Darth Vader Ducky"] += 1
    elif time <= 120:
        ducky["Thor Ducky"] += 1
    elif time <= 180:
        ducky["Big Blue Rubber Ducky"] += 1
    elif time <= 240:
        ducky["Small Yellow Rubber Ducky"] += 1
    else:
        tasks[-1] -= 2
        programmers_time.append(programmers_time.popleft())
        continue
    programmers_time.popleft()
    tasks.pop()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducky.items():
    print(f"{key}: {value}")


