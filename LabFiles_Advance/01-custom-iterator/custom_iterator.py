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
# custom_range = CustomRange(1, 10, 2)
# for number in custom_range:
#     print(number)  # Output: 1, 3, 5, 7, 9