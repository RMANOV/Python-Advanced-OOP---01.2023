# Even or Odd
# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. 
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.

def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [x for x in args[:-1] if x % 2 == 0]
    elif command == "odd":
        return [x for x in args[:-1] if x % 2 != 0]