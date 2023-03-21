# Reverse String
# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.


def reverse_text(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

