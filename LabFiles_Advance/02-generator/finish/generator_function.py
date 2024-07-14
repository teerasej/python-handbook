
# Using the generator function to read a large file line by line
file_path = 'large_log_file.txt'  # Path to a very large log file

def read_large_file(file_path):
    """Generator function to read a large file line by line."""
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


for line in read_large_file(file_path):
    print(line.strip())  # Process each line (e.g., print, store, analyze)