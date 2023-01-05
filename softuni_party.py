# SoftUni Party
# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. 
# When a guest comes, check if they exist on any of the two reservation lists.
# On the first line, you will receive the number of guests – N. 
# On the following N lines, you will be receiving their reservation codes. 
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit. 
# Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# •	The VIP guests must be first.
# •	Both the VIP and the Regular guests must be sorted in ascending order.

number_of_guests = int(input())
regular_guests = set()
vip_guests = set()

for _ in range(number_of_guests):
    guest = input()
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        regular_guests.add(guest)

while True:
    guest = input()
    if guest == "END":
        break
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)

# print(len(vip_guests) + len(regular_guests))
print(len(vip_guests.union(regular_guests)))

vip_guests = sorted(vip_guests)
for guest in vip_guests:
    print(guest)


regular_guests = sorted(regular_guests)
for guest in regular_guests:
    print(guest)
