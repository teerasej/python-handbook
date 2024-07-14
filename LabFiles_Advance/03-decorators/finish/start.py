
# define the decorator function
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper


# Test the decorated function
@log_function_call
def greet(name):
    return f"Hello, {name}!"

greet("Alice")