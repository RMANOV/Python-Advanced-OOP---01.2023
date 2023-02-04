# binary search algorithm without recursion

search_list = [
    1,
    3,
    5,
    30,
    42,
    43,
    500,
    1000,
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
    1008,
]
target = int(input("Enter a number: "))


def binary_search(search_list, target):
    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if search_list[mid] == target:
            return mid
        elif search_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


print(binary_search(search_list, target))
