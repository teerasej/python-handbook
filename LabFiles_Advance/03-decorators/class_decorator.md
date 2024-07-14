
# Example 3: Class Decorators 

In a real-world scenario, the Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. This is particularly useful in scenarios where you want to control access to a shared resource, such as a database connection or a configuration manager.

1. Open file `LabFiles_Advance/03-decorators/class_decorator.py`.
2. Take a look at the existing class.

```python

# Create a class decorator that will make sure that only one instance of the class is created.


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
```

3. Run the code using the command below.

```bash
python class_decorator.py
```
4. Observe the output, you will see it return False. because it is not the same instance.
5. Update the code in `LabFiles_Advance/03-decorators/class_decorator.py` to the following:

```python
# Create a class decorator that will make sure that only one instance of the class is created.
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
```

6. Apply the decorator to the DatabaseConnection class.

```python
# Apply the decorator to the DatabaseConnection class
@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Database Connection Established"

    def connect(self):
        return self.connection
```

7. Save file.
8. Right-click on the `03-decorators` folder and select `Open in integrated terminal`.
9. Run the code using the command below.

```bash
python class_decorator.py
```
10. Observe the output, you will see it return True. because it is the same instance.