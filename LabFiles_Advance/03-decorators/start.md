## Example 1: Simple Decorator

1. Open file `LabFiles_Advance/03-decorators/start.py`.
2. Take a look with a simple function that we will decorate.

```python
def greet(name):
    return f"Hello, {name}!"
```

3. Create a decorator function that logs the function call details.

```python
# define the decorator function

# The log_function_call function is a decorator. It takes a function func as an argument, which it will enhance with additional functionality.
def log_function_call(func):

    # The wrapper function is defined inside log_function_call. It will wrap the original function, adding extra behavior before and after the original function’s execution.

    # *args and **kwargs allow the wrapper function to accept any number of positional and keyword arguments, which are passed to the original function.
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} {kwargs}")
        
        # The original function func is called with the arguments *args and **kwargs.
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        
        # The wrapper function returns the result of the original function call, ensuring that the decorated function behaves like the original in terms of output.
        return result

    # The log_function_call function returns the wrapper function, effectively replacing the original function with the wrapper function that includes the additional logging functionality.
    return wrapper
```

4. Apply the decorator to the greet function.

```python
@log_function_call
def greet(name):
    return f"Hello, {name}!"

# Test the decorated function
greet("Alice")
```

5. Right-click on the `03-decorators` folder and select `Open in integrated terminal`.
6. Run the code using the command below.

```bash
python start.py
```

7. Observe the output.

### Explain 

```python
def greet(name):
    return f"Hello, {name}!"

# define the decorator function
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_function_call
def greet(name):
    return f"Hello, {name}!"

# Test the decorated function
greet("Alice")
```

- The log_function_call decorator takes a function func as an argument.
- It defines a wrapper function that logs the function call details and calls the original function.
- The wrapper function is returned, replacing the original function with the decorated version.
