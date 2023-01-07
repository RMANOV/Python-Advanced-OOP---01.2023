# Expression Evaluator
# Write a program that evaluates a string expression. 
# You will be given that string expression on the first line in the form of numbers and operators separated with a single space 
# from each other. Your job is to take that string expression and calculate the result after evaluating it.
# To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", 
# the first time we meet an operator (*), we should take all the numbers we have so far (2, 4), apply that operation to them, 
# and save the result (8). The next time we meet an operator (-), 
# we again take all the numbers we have (8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). 
# In the end, we print the result.
# All the numbers will always be integers, and the possible operators are "*", "+", "-", "/". 
# It is important to keep the order of the numbers (especially for "/" and "-" because the order matters).
# When having a division, you should round the result to the lower integer.
# Input
# •	Single line: a string containing integers and operators
# Output
# •	Single number: the result after the evaluation
# Constraints
# •	When reaching an operator, it is sure that you will have a minimum of one number to evaluate
# •	The string will always end with an operator, so you get one number as a result
# •	Operators and numbers will always be valid
# •	There will be no case of division by zero
# •	There might be negative numbers in the string


expression = input().split()

# Use a stack to store the numbers and operators
stack = []

# Precedence levels for the operators
precedence = {'*': 2, '/': 2, '+': 1, '-': 1}

for token in expression:
    if token in precedence:
        # Process the operators in the stack according to their precedence
        while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]:
            op = stack.pop()
            if len(stack) < 2:
                # Not enough elements in the stack to perform the operation
                break
            num2 = stack.pop()
            num1 = stack.pop()
            if op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 // num2
            elif op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            stack.append(result)
        stack.append(token)
    else:
        # Token is a number, just push it to the stack
        stack.append(int(token))

# Process the remaining operators in the stack
while len(stack) > 1:
    if len(stack) < 3:
        # Not enough elements in the stack to perform the operation
        break
    num2 = stack.pop()
    num1 = stack.pop()
    op = stack.pop()
    if op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 // num2
    elif op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    stack.append(result)

# The final result should be the only element in the stack
print(stack[0])




# expression = input().split()
# result = 0

# # Use a stack to store the numbers
# stack = []

# for token in expression:
#     if token in {"*", "/", "+", "-"}:
#         # Pop the last two numbers from the stack
#         num2 = stack.pop()
#         num1 = stack.pop()
#         if token == "*":
#             result = num1 * num2
#         elif token == "/":
#             result = num1 // num2
            
#         elif token == "+":
#             result = num1 + num2
#         elif token == "-":
#             result = num1 - num2
#         # Push the result back to the stack
#         stack.append(result)
#     else:
#         # Token is a number, just push it to the stack
#         stack.append(int(token))

# # The final result should be the only element in the stack
# print(stack[0])


# expression = input().split()
# result = 0

# for i in range(len(expression)):
#     if expression[i] == "*":
#         result = int(expression[i-2]) * int(expression[i-1])
#         expression[i-2] = result
#         expression.pop(i)
#         expression.pop(i-1)
#         break
#     elif expression[i] == "/":
#         result = int(expression[i-2]) / int(expression[i-1])
#         expression[i-2] = round(result)
#         expression.pop(i)
#         expression.pop(i-1)
#         break
#     elif expression[i] == "+":
#         result = int(expression[i-2]) + int(expression[i-1])
#         expression[i-2] = result
#         expression.pop(i)
#         expression.pop(i-1)
#         break
#     elif expression[i] == "-":
#         result = int(expression[i-2]) - int(expression[i-1])
#         expression[i-2] = result
#         expression.pop(i)
#         expression.pop(i-1)
#         break
# print(int(result))
