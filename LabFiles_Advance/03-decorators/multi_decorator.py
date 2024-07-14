import time

# define the decorator functions for timing and logging


# define the decorator functions for log function calls
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Apply multiple decorators to a function

@log_function_call
def greet(name):
    time.sleep(1)
    return f"Hello, {name}!"

# Test the decorated function
greet("Alice")