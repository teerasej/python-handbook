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