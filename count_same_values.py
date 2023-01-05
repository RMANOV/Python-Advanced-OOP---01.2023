# Count Same Values
# You will be given numbers separated by a space. 
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
# The number must be formatted to the first decimal point.

numbers = input().split()

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    number = float(number)
    print(f"{number:.1f} - {count} times")
