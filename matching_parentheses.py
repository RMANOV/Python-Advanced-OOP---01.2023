# # You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# # Print the result back on the console.
# Scan through the expression searching for parentheses:
# •	If you find an opening parenthesis, push the index into the stack.
# •	If you find a closing parenthesis, pop the topmost element from the stack. This is the index of the last opening parenthesis.
# •	Use the current index and the popped one to extract a set of parentheses.

initial_list = list(input())
stack = []

for i in range(len(initial_list)):
    if initial_list[i] == "(":
        stack.append(i)
    elif initial_list[i] == ")":
        start = stack.pop()
        end = i
        print("".join(initial_list[start : end + 1]))
