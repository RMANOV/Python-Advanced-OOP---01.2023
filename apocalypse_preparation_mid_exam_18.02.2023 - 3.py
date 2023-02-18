# Apocalypse Preparation
# You are in the middle of a zombie apocalypse and you want to go out for exploration.
# But before you do that, you need to prepare some healing items.
# On the first line, you will be given a sequence representing textiles. On the second line, you will be given another sequence,
# which represents medicaments.
# While both collections contain any elements, you will have to combine elements from the collections in order to create healing items.
# You should start by getting the first value of textile and the last value of medicaments:
# •	If their sum is equal to any of the items in the table below create that item and remove both values.
# •	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values,
# and add the remaining resources(of the sum) to the next value in the medicament collection
# (Take the element from the collection, add the remaining sum to it, and put the element back to its place).
# •	If you can’t create anything, remove the textile value, add 10 to the medicament value, and return the medicament back to its place, into its collection.
# You need to stop creating healing items when either the textile or the medicaments are exhausted.
# Healing item	Resources needed
# Patch	30
# Bandage	40
# MedKit	100
# In the end, you should print on the console message for the sequence that has ended, then the created items,
# and in the end the remaining items (if any).
# Input
# •	On the first line, you will receive a sequence of integers representing the textiles, separated by a single space (" ").
# •	On the second line, you will receive a sequence of integers representing the medicaments, separated by a single space (" ").
# Output
# •	On the first line print which one of the collections is over:
# o	If the textile is over print: "Textiles are empty."
# o	If the medicaments are over print: "Medicaments are empty."
# o	If both are empty print: "Textiles and medicaments are both empty."
# •	On the next n lines print only the created items (if any) ordered by the amount created descending, then by name alphabetically:
# "{item name} - {amount created}
#   {item name} - {amount created}
# …
# "
# Hint: Do not print items, which are not created.
# •	On the last line print the remaining items(if any):
# o	If there are any medicaments left:
#  "Medicaments left: …{medicament2}, {medicament1}"
# o	If there are any textiles left:
# "Textiles left: {textile1}, {textile2}…"
# Constraints
# •	All the numbers will be in the range [0…1000].
# •	All the inputs will be valid.


from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))
created = {"Patch": 0, "Bandage": 0, "MedKit": 0}
part = 0

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()+part
    part = 0

    total = textile + medicament
    if total == 30:
        created["Patch"] += 1
    elif total == 40:
        created["Bandage"] += 1
    elif total >= 100:
        created["MedKit"] += 1
        if total > 100:
            part = (medicament + textile - 100)
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    for item, amount in sorted(created.items(), key=lambda x: (-x[1], x[0])):
        if amount > 0:
            print(f"{item} - {amount}")
elif not textiles:
    print("Textiles are empty.")
    for item, amount in sorted(created.items(), key=lambda x: (-x[1], x[0])):
        if amount > 0:
            print(f"{item} - {amount}")
    medicaments.reverse()
    print("Medicaments left:", ", ".join(map(str, medicaments)))
else:
    print("Medicaments are empty.")
    for item, amount in sorted(created.items(), key=lambda x: (-x[1], x[0])):
        if amount > 0:
            print(f"{item} - {amount}")
    print("Textiles left:", ", ".join(map(str, textiles)))
