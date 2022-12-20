# Tom is working at the supermarket, and he needs your help to keep track of his clients. 
# Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. 
# If, in the meantime, you receive the command "Paid", you should print each customer in the order they are served (from the first to the last one) and empty the queue. 
# When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining."

import collections

queue = collections.deque()
while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
