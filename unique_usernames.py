# Unique Usernames
# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. 
# On the first line, you will receive an integer N. On the next N lines, you will receive a username. 
# Print the collection on the console (the order does not matter):

number_of_usernames = int(input())
unique_usernames = set()

for _ in range(number_of_usernames):
    unique_usernames.add(input())

[print(username) for username in unique_usernames]


