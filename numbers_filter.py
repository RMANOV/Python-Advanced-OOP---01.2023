# Numbers Filter
# Create a function called even_odd_filter() that can receive a different number of named arguments. 
# The keys will be "even" and/or "odd", and the values will be a list of numbers.  
# When the key is "odd", you should extract only the odd numbers from its list. 
# When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order.

def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "odd":
            result[key] = [x for x in value if x % 2 != 0]
        elif key == "even":
            result[key] = [x for x in value if x % 2 == 0]
    return dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))