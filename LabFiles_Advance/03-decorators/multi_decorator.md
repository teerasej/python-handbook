
## Example 2: Multiple Decorators 

1. Open file `LabFiles_Advance/03-decorators/start.py`.
2. Take a look with an existing decorator function that logs the function call details.

```python
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
```

3. Create a new decorator function that logs the time taken to execute the function.

```python
# define the decorator functions for timing and logging
def time_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' execution time: {end_time - start_time} seconds")
        return result
    return wrapper
```

4. Apply the new decorator to the greet function.

```python
# Apply multiple decorators to a function
@time_function_call
@log_function_call
def greet(name):
    time.sleep(1)
    return f"Hello, {name}!"
```

5. Save file.
6. Right-click on the `03-decorators` folder and select `Open in integrated terminal`.
7. Run the code using the command below.

```bash
python multi_decorator.py
```

8. Observe the output.

## Explanation:

- Both log_function_call and time_function_call are applied to the greet function.
- The time_function_call decorator is applied first, followed by log_function_call.
- The function call is logged, then timed, and the execution time is printed.

> Note: The order of decorators matters. The last decorator applied is the first one executed.