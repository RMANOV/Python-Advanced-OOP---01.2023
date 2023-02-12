# Cheese Showcase
# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. 
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). 
# For each kind of cheese, return their pieces quantities in descending order.

def sorting_cheeses(**kwargs):
    # get data from kwargs and create a dict with the data - keys and lists of values
        # get keys and store them in a list
        # get values and store them in a list
        # create a dict with the keys and values
    # sort dict by values
    # sort dict by keys
    # create a list with the sorted dict
    # print the result in the required format

    
    # print '\n'.join([str(cheese) for cheese in sorted_cheeses])

    # return '\n'.join([str(cheese) for cheese in result])


def sorting_cheeses(**kwargs):
    # Get data from kwargs and create a dictionary with the data - keys and lists of values
    cheeses = {}
    for cheese, quantities in kwargs.items():
        cheeses[cheese] = quantities
    
    # Sort the dictionary by values (number of pieces of each cheese) in descending order and by keys (cheese names) in ascending order
    sorted_cheeses = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))
    
    # Format the result and return it as a string
    result = []
    for cheese, quantities in sorted_cheeses:
        result.append(cheese)
        result.extend(sorted(quantities, reverse=True))
    return '\n'.join([str(item) for item in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
