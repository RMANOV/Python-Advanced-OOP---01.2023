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

chocolate = [int(x) for x in input().split(", ")]
milk = [int(x) for x in input().split(", ")]

for i in range(len(chocolate)):
    chocolate[i] -= 5
    if chocolate[i] <= 0:
        chocolate.pop(i)
        i -= 1

while len(chocolate) > 0 and len(milk) > 0:
    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.pop(0)
    else:
        milk.append(milk.pop(0))
        chocolate[-1] -= 5
        if chocolate[-1] <= 0:
            chocolate.pop()

if len(chocolate) == 0:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if len(chocolate) == 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")

if len(milk) == 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join([str(x) for x in milk])}")