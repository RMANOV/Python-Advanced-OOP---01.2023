# Cheese Showcase
# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. 
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). 
# For each kind of cheese, return their pieces quantities in descending order.

def sorting_cheeses(**kwargs):
    cheeses = {}
    for cheese, quantity in kwargs.items():
        cheeses[cheese] = sum(quantity)
    sorted_cheeses = sorted(cheeses.items(), key=lambda x: (-x[1], x[0]))
    return sorted_cheeses