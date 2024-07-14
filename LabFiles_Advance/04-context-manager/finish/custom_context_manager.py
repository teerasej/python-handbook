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