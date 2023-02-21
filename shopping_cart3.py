# Shopping Cart
# Peter has decided to invite some guests. He should go shopping, but he will need help because
# there are too many things he needs to remember. Would you assist him?
# Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:
# "Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
# •	Soup: 3
# •	Pizza: 4
# •	Dessert: 2
# Once you reach the limit of a meal, you should stop adding products to that meal.
# The function will receive a different number of arguments.
# The arguments will be passed as tuples with two elements - the first one is the type of meal,
# and the second is the product for the meal.
# You need to take each argument and make a dictionary with the meal's name as a key and the products as a value of the corresponding key.
# There are some additional requirements:
# •	If you receive the same product for the same meal more than once, you must not add it again.
# •	If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart -
# just sort and return the desired result as described below.
# In the end, sort the meals by the number of bought products in descending order.
# If there are meals with an equal number of products, sort them (the meals) by their name in ascending order (alphabetically).
# For each meal sort its products in ascending order (alphabetically).
# Return an output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	Return a string for each of the 3 types of a meal of the sorted result in the format:
# o	"{meal_type}:"
# " - {first_product_added}"
# " - {second_product_added}"
#  …
# " - {Nth_product_added}"
# o	If there are no products given for a meal, return just its name in the format shown above.
# •	If there are NO products in the cart (at all), return the message: "No products in the cart!"
# Constrains
# •	Each tuple given will always contain the type of meal in the first position and a product in the second.
# •	There will be no other meals passed than "Soup", "Pizza", and "Dessert".


def shopping_cart(*args):
    cart = {"Pizza": [], "Soup": [], "Dessert": []}

    for tuple_ in args:
        meal = tuple_[0]
        product = tuple_[1]
        if tuple_ == "Stop":
            break
        if meal == "Pizza" and len(cart["Pizza"]) == 4:
            continue
        elif meal == "Soup" and len(cart["Soup"]) == 3:
            continue
        elif meal == "Dessert" and len(cart["Dessert"]) == 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)
    if not any(cart.values()):
        return "No products in the cart!"
    
    for key, value in cart.items():
        value.sort()
    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for tuple_ in sorted_cart:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"
    return result
   


print(
    shopping_cart(
        ("Pizza", "ham"),
        ("Soup", "carrots"),
        ("Pizza", "cheese"),
        ("Pizza", "flour"),
        ("Dessert", "milk"),
        ("Pizza", "mushrooms"),
        ("Pizza", "tomatoes"),
        "Stop",
    )
)
