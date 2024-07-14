## Example 2: Simple Custom Iterator

1. Open file `LabFiles_Advance/01-custom-iterator/custom_iterator.py`.
2. write the code below into the file.

```python
# Custom iterator class to iterate over a range of numbers with a specific step
class CustomRange:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current

# Using the custom iterator
print("\nUsing the custom iterator")
custom_range = CustomRange(1, 10, 2)
for number in custom_range:
    print(number)  # Output: 1, 3, 5, 7, 9
```

3. Right click on the `01-custom-iterator` folder and select `Open in integrated terminal`.
4. Run the code using the command below.

```bash
python custom_iterator.py
```

5. Observe the output.