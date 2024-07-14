
# Custom Context Manager

1. Open file `LabFiles_Advance/04-context-manager/custom_context_manager.py` in a code editor.
2. Create a class named `CustomContextManager` that implements the `__enter__` and `__exit__` methods.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```

3. Use the `with` statement to open a file using the `CustomContextManager` class.

```python
with FileManager('example.txt', 'w') as file:
    file.write('Hello, World!')
```

4. Save the file
5. Run the script using the following command:

```bash
python custom_context_manager.py
```
6. Verify that the file `example.txt` is created and contains the text `Hello, World!`.

## Explanation

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # __enter__ and __exit__ are the two methods that are required to implement a context manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # __exit__ method is called when the block of code inside the with statement is executed
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        
        
with FileManager('example.txt', 'w') as file:
    file.write('Hello, World!')
```

The __enter__ method opens the file and returns it, while the __exit__ method ensures the file is closed after the with block is executed, even if an error occurs.
