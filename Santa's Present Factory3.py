# Santa's Present Factory
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
# After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400
# You should take the last box with materials and the first magic level value to craft a toy.
# Their multiplication calculates the total magic level.
# If the result equals one of the levels described in the table above,
# you craft the present and remove both materials and magic value.
# Otherwise:
# •	If the product of the operation is a negative number, you should sum the values together,
# remove them both from their positions, and add the result to the materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive number,
# remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle
# Input
# •	The first line of input will represent the values of boxes with materials - integers, separated by a single space
# •	On the second line, you will be given the magic values - integers again, separated by a single space
# Output
# •	On the first line - print whether you've succeeded in crafting the presents:
# o	"The presents are crafted! Merry Christmas!"
# o	"No presents this Christmas!"
# •	On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
# o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
# o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
# •	On the next lines print the presents you have crafted, ordered alphabetically in the format:
# o	"{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"

from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]

# from collections import deque, defaultdict

# materials = deque([int(x) for x in input().split()])
# magic = deque([int(x) for x in input().split()])
# presents = defaultdict(int)

# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     if m <= 0 or ma <= 0:
#         if m <= 0:
#             materials.append(m)
#         if ma <= 0:
#             magic.append(ma)
#         continue
#     product = m * ma
#     if product < 0:
#         sum_val = m + ma
#         materials.append(sum_val)
#         # remove both
#         magic.popleft()
#         materials.pop()
#     elif product > 0 and product not in [150, 250, 300, 400]:
#         materials.append(m + 15)
#         magic.popleft()
#     elif product > 0 and product in [150, 250, 300, 400]:
#         if product >= 150 and product < 250:
#             presents["Doll"] += 1
#             materials.pop()
#             magic.popleft()
#         elif product >= 250 and product < 300:
#             presents["Wooden train"] += 1
#             materials.pop()
#             magic.popleft()
#         elif product >= 300 and product < 400:
#             presents["Teddy bear"] += 1
#             materials.pop()
#             magic.popleft()
#         elif product >= 400:
#             presents["Bicycle"] += 1
#             materials.pop()
#             magic.popleft()

# if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
#     presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print(f"Materials left: {', '.join(map(str, materials))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# for k, v in sorted(presents.items()):
#     print(f"{k}: {v}")


# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     if m <= 0 or ma <= 0:
#         if m <= 0:
#             materials.append(m)
#         if ma <= 0:
#             magic.append(ma)
#         continue
#     product = m * ma
#     if product == 150:
#         presents["Doll"] += 1
#         materials.pop()
#         magic.popleft()
#     elif product == 250:
#         presents["Wooden train"] += 1
#         materials.pop()
#         magic.popleft()
#     elif product == 300:
#         presents["Teddy bear"] += 1
#         materials.pop()
#         magic.popleft()
#     elif product == 400:
#         presents["Bicycle"] += 1
#         materials.pop()
#         magic.popleft()
#     elif product < 0:
#         sum_val = m + ma
#         materials.append(sum_val)
#         # remove both
#         magic.popleft()
#         materials.pop()
#     elif product > 0 and product not in [150, 250, 300, 400]:
#         materials.append(m + 15)
#         magic.popleft()

if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
    presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for present in sorted(presents.keys()):
    if presents[present] > 0:
        print(f"{present}: {presents[present]}")


# from collections import deque

# materials = deque([int(x) for x in input().split()])
# magic = deque([int(x) for x in input().split()])
# presents = {"Doll": [0, 150], "Wooden train": [0, 250], "Teddy bear": [0, 300], "Bicycle": [0, 400]}

# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     if m <= 0 or ma <= 0:
#         if m <= 0:
#             materials.append(m)
#         if ma <= 0:
#             magic.append(ma)
#         continue
#     product = m * ma
#     for present, val in presents.items():
#         if product >= val[1] and product <= val[1]+50:
#             presents[present][0] += 1
#             break
#     else:
#         if product < 0:
#             sum_val = m + ma
#             materials.append(sum_val)
#         elif product > 0:
#             materials.append(m + 15)

# if (presents["Doll"][0] >= 1 and presents["Wooden train"][0] >= 1) or (
#     presents["Teddy bear"][0] >= 1 and presents["Bicycle"][0] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print(f"Materials left: {', '.join(map(str, materials))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# for present in sorted(presents.keys()):
#     if presents[present][0] > 0:
#         print(f"{present}: {presents[present][0]}")


# materials = deque([int(x) for x in input().split()])
# magic = deque([int(x) for x in input().split()])
# presents = defaultdict(int)

# for m in materials:
#     if m == 0:
#         materials.remove(m)
# for ma in magic:
#     if ma == 0:
#         magic.remove(ma)


# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     if m == 0 or ma == 0:
#         if m == 0:
#             materials.append(m)
#         if ma == 0:
#             magic.append(ma)
#         continue
#     product = m * ma
#     if product == 150:
#         presents["Doll"] += 1
#     elif product == 250:
#         presents["Wooden train"] += 1
#     elif product == 300:
#         presents["Teddy bear"] += 1
#     elif product == 400:
#         presents["Bicycle"] += 1
#     elif product < 0:
#         sum_val = m + ma
#         materials.append(sum_val)
#     elif product > 0:
#         materials.append(m + 15)

# if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
#     presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print(f"Materials left: {', '.join(map(str, materials))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# for present in sorted(presents.keys()):
#     if presents[present] > 0:
#         print(f"{present}: {presents[present]}")


# materials = deque([int(x) for x in input().split()])
# magic = input().split()
# presents = defaultdict(int)


# if materials and magic:
#     while materials and magic:
#         m = materials.pop()
#         ma = magic.pop()
#         if m == 0 or ma == 0:
#             if m == 0:
#                 materials.append(m)
#             if ma == 0:
#                 magic.append(ma)
#             continue
#         product = m * ma
#         if product == 150:
#             presents["Doll"] += 1
#         elif product == 250:
#             presents["Wooden train"] += 1
#         elif product == 300:
#             presents["Teddy bear"] += 1
#         elif product == 400:
#             presents["Bicycle"] += 1
#         elif product < 0:
#             sum_val = m + ma
#             materials.append(sum_val)
#         elif 0 < product < 150:
#             materials.append(m + 15)

# if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
#     presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# # if materials are 0 do not print them
# if materials:
#     print(f"Materials left: {', '.join(map(str, materials))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# if presents:
#     for present in sorted(presents.keys()):
#         if presents[present] > 0:
#             print(f"{present}: {presents[present]}")


# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     if m == 0 or ma == 0:
#         if m == 0:
#             materials.append(m)
#         if ma == 0:
#             magic.append(ma)
#         continue
#     product = m * ma
#     if product == 150:
#         presents["Doll"] += 1
#     elif product == 250:
#         presents["Wooden train"] += 1
#     elif product == 300:
#         presents["Teddy bear"] += 1
#     elif product == 400:
#         presents["Bicycle"] += 1
#     elif product < 0:
#         sum_val = m + ma
#         materials.append(sum_val)
#     elif product > 0:
#         materials.append(m + 15)

# if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
#     presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print(f"Materials left: {', '.join(map(str, materials))}")

# if magic:
#     print(f"Magic left: {', '.join(map(str, magic))}")

# for present in sorted(presents.keys()):
#     if presents[present] > 0:
#         print(f"{present}: {presents[present]}")


# while materials and magic:
#     m = materials.pop()
#     ma = magic.popleft()
#     product = m * ma
#     if product == 150:
#         presents["Doll"] += 1
#     elif product == 250:
#         presents["Wooden train"] += 1
#     elif product == 300:
#         presents["Teddy bear"] += 1
#     elif product == 400:
#         presents["Bicycle"] += 1
#     elif product < 0:
#         sum_val = m + ma
#         materials.append(sum_val)
#     elif product > 0:
#         materials.append(m + 15)
#     if product == 0 or product < 0:
#         if m == 0:
#             materials.append(m)
#         if ma == 0:
#             magic.append(ma)

# if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or (
#     presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

# if materials:
#     print("Materials left: " + ", ".join(map(str, materials)))

# if magic:
#     print("Magic left: " + ", ".join(map(str, magic)))

# if presents:
#     for present in sorted(presents.keys()):
#         if presents[present] > 0:
#             print(f"{present}: {presents[present]}")


# # Helper function to check if we have crafted a doll and a train or a teddy bear and a bicycle
# def check_presents(presents):
#     if (presents["Doll"] >= 1 and presents["Wooden train"] >= 1) or \
#        (presents["Teddy bear"] >= 1 and presents["Bicycle"] >= 1):
#         return True
#     else:
#         return False

# def craft_presents(materials, magic):
#     materials = deque(materials)
#     magic = deque(magic)
#     presents = defaultdict(int)
#     while materials and magic:
#         m = materials.pop()
#         ma = magic.popleft()
#         product = m * ma
#         if product == 150:
#             presents["Doll"] += 1
#         elif product == 250:
#             presents["Wooden train"] += 1
#         elif product == 300:
#             presents["Teddy bear"] += 1
#         elif product == 400:
#             presents["Bicycle"] += 1
#         elif product < 0:
#             sum_val = m + ma
#             materials.append(sum_val)
#         elif product > 0:
#             materials.append(m+15)
#         if product == 0 or product < 0:
#             if m == 0:
#                 materials.append(m)
#             if ma == 0:
#                 magic.append(ma)
#     return materials, magic, presents

#     # if check_presents(presents):
#     #     print("The presents are crafted! Merry Christmas!")
#     # else:
#     #     print("No presents this Christmas!")
#     # if materials:
#     #     print("Materials left: " + ", ".join(map(str, materials)))
#     # if magic:
#     #     print("Magic left: " + ", ".join(map(str, magic)))
#     # for present in sorted(presents.keys()):
#     #     print("{}: {}".format(present, presents[present]))

# materialss = [int(x) for x in input().split()]
