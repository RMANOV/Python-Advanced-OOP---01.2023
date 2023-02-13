# Function Executor
# Create a function called func_executor() that can receive a different number of tuples,
# each of which will have exactly 2 elements: the first will be a function, 
# and the second will be a tuple of the arguments that need to be passed to that function.
# You should execute each function and return its result in the format:
# "{function name} - {function result}"

def func_executor(*args):
    result = []
    for func, arg in args:
        result.append(f"{func.__name__} - {func(*arg)}")
    return '\n'.join(result)
