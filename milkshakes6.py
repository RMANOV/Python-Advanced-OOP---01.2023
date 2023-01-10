# Milkshakes
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start with the last chocolate and try to match it with the first cup of milk.
# If their values are equal, you should make a milkshake and remove both ingredients.
# Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0,
# you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left,
# you need to stop making chocolate milkshakes.
# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# •	On the first line, print:
# o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
# o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
# o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o	Otherwise: "Milk: empty"

# chocolate = [int(x) for x in input().split(", ")]
# milk = [int(x) for x in input().split(", ")]
# milkshakes = 0

from collections import deque

chocolate_stack = [int(x) for x in input().split(", ")]
milk_queue = deque([int(x) for x in input().split(", ")])
milkshakes = 0


for i in range(len(chocolate_stack) - 1, -1, -1):
    if chocolate_stack[i] <= 0:
        chocolate_stack.pop(i)
    else:
        break

for i in range(len(milk_queue)):
    if milk_queue[i] <= 0:
        milk_queue.popleft()
    else:
        break

while chocolate_stack and milk_queue and milkshakes != 5:
    current_chocolate = chocolate_stack.pop()
    current_cup = milk_queue.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue
    elif current_chocolate <= 0:
        milk_queue.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolate_stack.append(current_chocolate)
        continue
    if current_chocolate == current_cup:
        milkshakes += 1
    else:
        milk_queue.append(current_cup)
        chocolate_stack.append(current_chocolate - 5)






# while chocolate_stack and milk_queue and milkshakes != 5:
#     current_chocolate = chocolate_stack.pop()
#     current_cup = milk_queue.popleft()

#     if current_chocolate <= 0 and current_cup <= 0:
#         continue
#     elif current_chocolate <= 0:
#         milk_queue.appendleft(current_cup)
#         continue
#     elif current_cup <= 0:
#         chocolate_stack.append(current_chocolate)
#         continue
#     if current_chocolate == current_cup:
#         milkshakes += 1
#     else:
#         milk_queue.append(current_cup)
#         chocolate_stack.append(current_chocolate - 5)


# while chocolate_stack and milk_queue:
#     if chocolate_stack[-1] == milk_queue[0]:
#         chocolate_stack.pop()
#         milk_queue.popleft()
#         milkshakes += 1
#         if milkshakes == 5:
#             break
#     else:
#         milk_queue.append(milk_queue.popleft())
#         chocolate_stack[-1] -= 5
#         if chocolate_stack[-1] <= 0:
#             chocolate_stack.pop()


if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if len(chocolate_stack) == 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_stack])}")

if len(milk_queue) == 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join([str(x) for x in milk_queue])}")


# while len(chocolate) > 0 and len(milk) > 0:
#     if chocolate[-1] == milk[0]:
#         if len(chocolate) == 1 and len(milk) == 1:
#             break
#         chocolate.pop()
#         milk.pop(0)
#         milkshakes += 1
#         if milkshakes == 5:
#             break
#     else:
#         milk.append(milk.pop(0))
#         chocolate[-1] -= 5
#         if chocolate[-1] <= 0:
#             chocolate.pop()


# if len(chocolate) == 0 or len(milk) == 0 or milkshakes < 5:
#     print("Not enough milkshakes.")
# else:
#     print("Great! You made all the chocolate milkshakes needed!")

# if not chocolate:
#     print("Chocolate: empty")
# else:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")

# if not milk:
#     print("Milk: empty")
# else:
#     print(f"Milk: {', '.join([str(x) for x in milk])}")

# def milkshakess(chocolate, milk):
#     milkshakes = 0
#     while len(chocolate) > 0 and len(milk) > 0:
#         if chocolate[-1] == milk[0]:
#             if len(chocolate) == 1 and len(milk) == 1:
#                 break
#             chocolate.pop()
#             milk.pop(0)
#             milkshakes += 1
#             if milkshakes == 5:
#                 break
#         else:
#             milk.append(milk.pop(0))
#             chocolate[-1] -= 5
#             if chocolate[-1] <= 0:
#                 chocolate.pop()
#     chocolate = [x for x in chocolate if x > 0]
#     milk = [x for x in milk if x > 0]
#     if len(chocolate) == 0 or len(milk) == 0 or milkshakes < 5:
#         print("Not enough milkshakes.")
#     else:
#         print("Great! You made all the chocolate milkshakes needed!")
#     if len(chocolate) == 0:
#         print("Chocolate: empty")
#     else:
#         print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
#     if len(milk) == 0:
#         print("Milk: empty")
#     else:
#         print(f"Milk: {', '.join([str(x) for x in milk])}")

# def main():
#     chocolate = [int(x) for x in input().split(", ")]
#     milk = [int(x) for x in input().split(", ")]
#     milkshakess(chocolate, milk)

# if __name__ == "__main__":
#     main()


# while len(chocolate) > 0 and len(milk) > 0:
#     # if values are equal
#     if chocolate[-1] == milk[0]:
#         # check if last element
#         if len(chocolate) == 1 and len(milk) == 1:
#             break
#         chocolate.pop()
#         milk.pop(0)
#         milkshakes += 1
#         if milkshakes == 5:
#             break
#     else:
#         milk.append(milk.pop(0))
#         chocolate[-1] -= 5
#         # if negative, remove chocolate
#         if chocolate[-1] <= 0:
#             chocolate.pop()

# # remove negative chocolates
# chocolate = [x for x in chocolate if x > 0]
# milk = [x for x in milk if x > 0]

# if len(chocolate) == 0 or len(milk) == 0 or milkshakes < 5:
#     print("Not enough milkshakes.")
# else:
#     print("Great! You made all the chocolate milkshakes needed!")

# if len(chocolate) == 0:
#     print("Chocolate: empty")
# else:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")

# if len(milk) == 0:
#     print("Milk: empty")
# else:
#     print(f"Milk: {', '.join([str(x) for x in milk])}")


# while len(chocolate) > 0 and len(milk) > 0:
#     if chocolate[-1] == milk[0]:
#         if len(chocolate) == 1 and len(milk) == 1:
#             break
#         chocolate.pop()
#         milk.pop(0)
#         milkshakes += 1
#         if milkshakes == 5:
#             break
#     else:
#         milk.append(milk.pop(0))
#         chocolate[-1] -= 5
#         if chocolate[-1] <= 0:
#             chocolate.pop()


# # for i in range(len(chocolate)):
# #     chocolate[i] -= 5
# #     if chocolate[i] <= 0:
# #         if i == len(chocolate) - 1:
# #             chocolate.pop()
# #         else:
# #             chocolate.pop(i)
# #             i -= 1


# # while len(chocolate) > 0 and len(milk) > 0:
# #     if chocolate[-1] == milk[0]:
# #         if len(chocolate) == 1 and len(milk) == 1:
# #             break
# #         chocolate.pop()
# #         milk.pop(0)
# #     else:
# #         milk.append(milk.pop(0))
# #         chocolate[-1] -= 5
# #         if chocolate[-1] <= 0:
# #             chocolate.pop()

# if len(chocolate) == 0 or len(milk) == 0 or milkshakes < 5:
#     print("Not enough milkshakes.")
# else:
#     print("Great! You made all the chocolate milkshakes needed!")

# if len(chocolate) == 0:
#     print("Chocolate: empty")
# else:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")

# if len(milk) == 0:
#     print("Milk: empty")
# else:
#     print(f"Milk: {', '.join([str(x) for x in milk])}")
