# Longest Intersection
# Write a program that finds the longest intersection. 
# You will be given the number N. On each of the next N lines, 
# you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". 
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
# Finally, you should find the longest intersection of all N intersections, 
# print the numbers that are included and its length in the format: 
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one

number_of_lines = int(input())

for i in range(number_of_lines):
    first_range, second_range = input().split('-')
    first_range_start, first_range_end = [int(x) for x in first_range.split(',')]
    second_range_start, second_range_end = [int(x) for x in second_range.split(',')]

    first_range_set = set(range(first_range_start, first_range_end + 1))
    second_range_set = set(range(second_range_start, second_range_end + 1))

    intersection = first_range_set & second_range_set

    if i == 0:
        longest_intersection = intersection
    else:
        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection

# print(longest_intersection)
print(f'Longest intersection is [{", ".join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}')
