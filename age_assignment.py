# Age Assignment
# Create a function called age_assignment() that receives a different number of names and a different number of key-value pairs. 
# The key will be a single letter (the first letter of each name) and the value - a number (age). 
# Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in the format: 
# "{name} is {age} years old."

def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                result[name] = age
    return '\n'.join([f"{k} is {v} years old." for k, v in sorted(result.items())])
