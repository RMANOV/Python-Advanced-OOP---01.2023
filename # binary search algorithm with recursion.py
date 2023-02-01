# binary search algorithm with recursion

my_list = [
    1,
    3,
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
    21,
    23,
    25,
    27,
    29,
    31,
    33,
    35,
    37,
    39,
    41,
    43,
    45,
    47,
    49,
    51,
    53,
    55,
    57,
    59,
    61,
    63,
    65,
    67,
    69,
    71,
    73,
    75,
    77,
    79,
    81,
    83,
    85,
    87,
    89,
    91,
    93,
    95,
    97,
    99,
]
target = int(input("Enter a number: "))


def binary_search(list, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if list[mid] == target:
        return True
    elif list[mid] > target:
        return binary_search(list, target, start, mid - 1)
    else:
        return binary_search(list, target, mid + 1, end)
