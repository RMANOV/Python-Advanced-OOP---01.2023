# Count Symbols
# Write a program that reads a text from the console and counts the occurrences of each character in it. 
# Print the results in alphabetical (lexicographical) order.

initial_text = input()
letters = set(initial_text)

for letter in sorted(letters):
    print(f"{letter}: {initial_text.count(letter)} time/s")

