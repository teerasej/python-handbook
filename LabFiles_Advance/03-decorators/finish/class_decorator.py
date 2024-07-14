
# Create a class decorator that will make sure that only one instance of the class is created.
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


# Apply the decorator to the DatabaseConnection class
@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Database Connection Established"

    def connect(self):
        return self.connection
    

# Test the Singleton behavior
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connect())
print(db2.connect())
print(db1 is db2)  # This should print True