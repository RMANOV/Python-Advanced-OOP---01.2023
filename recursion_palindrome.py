# Recursion Palindrome
# Write a recursive function called palindrome() that will receive a word and an index (always 0). 
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and 
# "{word} is not a palindrome" if the word is not a palindrome using recursion. 

def palindrome(word, index):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"
