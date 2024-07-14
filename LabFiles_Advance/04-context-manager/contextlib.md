
# Utilizing contextlib for Simpler Context Manager Implementation

1. Open file `LabFiles_Advance/04-context-manager/contextlib.py` in a code editor.
2. Import the `contextlib` module.

```python
from contextlib import contextmanager
```

3. Use the `contextlib.contextmanager` decorator to create a context manager.

```python

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()
```

The @contextmanager decorator turns a generator function into a context manager. The code before yield is equivalent to __enter__, and the code after yield is equivalent to __exit__. The yield statement is used to return the file object to the caller, and the finally block ensures that the file is closed after the with block is executed.

4. Use the `with` statement to open a file using the `open_file` context manager.

```python
with open_file('example.txt', 'w') as file:
    file.write('Hello, world from context lib!')
``` 

5. Save the file
6. Run the script using the following command:

```bash
python contextlib.py
```

7. Verify that the file `example.txt` is created and contains the text `Hello, world from context lib!`.

## complete code 

```python
from contextlib import contextmanager

# Define a context manager using the contextmanager decorator
@contextmanager
def open_file(filename, mode):
    # This line is equivalent to the __enter__ method
    file = open(filename, mode)
    try:
        yield file
        
    # This line is equivalent to the __exit__ method
    finally:
        file.close()
        
with open_file('example.txt', 'w') as file:
    file.write('Hello, world!')
```