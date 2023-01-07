# Battle of Names
# You will receive a number N. On the following N lines, you will be receiving names. 
# You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ". 
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set



number_of_names = int(input())

odd_set = set()
even_set = set()

for i in range(1, number_of_names + 1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)
    ascii_sum = ascii_sum // i
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    # print the union of the values, separated by ", "
    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
else:
    result = even_set.difference(odd_set)

print(", ".join([str(x) for x in result]))



# number_of_names = int(input())

# ascii_sum_odd = 0
# ascii_sum_even = 0

# for i in range(1, number_of_names + 1):
#     name = input()
#     ascii_sum = 0
#     for letter in name:
#         ascii_sum += ord(letter)
#     ascii_sum = ascii_sum // i
#     if ascii_sum % 2 == 0:
#         ascii_sum_even += ascii_sum
#     else:
#         ascii_sum_odd += ascii_sum

# if ascii_sum_even == ascii_sum_odd:
#     # print the union of the values, separated by ", "
#     print(", ".join([str(x) for x in range(ascii_sum_even + 1)]))
# elif ascii_sum_even > ascii_sum_odd:
#     print(", ".join([str(x) for x in range(ascii_sum_even + 1, ascii_sum_odd)]))
# else:
#     print(", ".join([str(x) for x in range(ascii_sum_odd + 1, ascii_sum_even)]))




# ascii_sum_odd = 0
# ascii_sum_even = 0

# for i in range(1, number_of_names + 1):
#     name = input()
#     ascii_sum = 0
#     for letter in name:
#         ascii_sum += ord(letter)
#     ascii_sum = ascii_sum // i
#     if ascii_sum % 2 == 0:
#         ascii_sum_even += ascii_sum
#     else:
#         ascii_sum_odd += ascii_sum

# if ascii_sum_even == ascii_sum_odd:
#     print(ascii_sum_even)
# elif ascii_sum_even > ascii_sum_odd:
#     print(ascii_sum_even - ascii_sum_odd)
# else:
#     print(ascii_sum_odd - ascii_sum_even)
