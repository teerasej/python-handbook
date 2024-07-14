
# Generator 

Imagine you are developing a data processing application that needs to read and process a very large log file line by line. Loading the entire file into memory is impractical due to its size. Using a generator allows you to read and process the file efficiently without consuming a large amount of memory.

## Example 1: Default Generator

1. Open file `LabFiles_Advance/02-custom-iterator/start.py`.
2. write the code below into the file.

```python
# Simple example of a generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

1. Right click on the `02-generator` folder and select `Open in integrated terminal`.
2. Run the code using the command below.

```bash
python start.py
```

5. Observe the output.

## Example 2: Simple Custom Iterator

1. Open file `LabFiles_Advance/02-custom-iterator/generator-function.py`.
2. write the code below into the file.

```python
def read_large_file(file_path):
    """Generator function to read a large file line by line."""
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line

# Using the generator function to read a large file line by line
file_path = 'large_log_file.txt'  # Path to a very large log file

for line in read_large_file(file_path):
    print(line.strip())  # Process each line (e.g., print, store, analyze)
```

3. Right click on the `01-custom-iterator` folder and select `Open in integrated terminal`.
4. Run the code using the command below.

```bash
python custom_iterator.py
```

5. Observe the output.

### Benefits of Using Generators for This Use Case:

1.	Memory Efficiency: Only one line of the file is read into memory at a time, making it suitable for processing very large files.
2.	Lazy Evaluation: The generator produces items only when requested, allowing for efficient handling of large datasets.
3.	Simplicity: The generator function encapsulates the logic for reading the file, making the code cleaner and more modular.