

# Example 3: Custom Iterator for Paginated Records


1. Open file `LabFiles_Advance/01-custom-iterator/paginated_iterator.py`.
2. write the code below into the file.

```python
class PaginatedRecords:
    def __init__(self, data_source, page_size=100):
        self.data_source = data_source
        self.page_size = page_size
        self.current_page = 0
        self.total_records = self._get_total_records()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        if start_index >= self.total_records:
            raise StopIteration
        self.current_page += 1
        return self._fetch_records(start_index, end_index)
    
    def _get_total_records(self):
        # Simulate getting total record count from the data source
        return len(self.data_source)
    
    def _fetch_records(self, start, end):
        # Simulate fetching records from the data source
        return self.data_source[start:end]

# Simulate a large dataset
data_source = [f"Record {i}" for i in range(1000)]

# Using the custom iterator for paginated records
paginated_records = PaginatedRecords(data_source)
for page in paginated_records:
    print(page)  # Output: Pages of 100 records each
```

3. Right click on the `01-custom-iterator` folder and select `Open in integrated terminal`.
4. Run the code using the command below.

```bash
python paginated_iterator.py
```

5. Observe the output.

### Explanation

- Custom Iterator Class: PaginatedRecords is designed to handle pagination.
- Initialization: It takes the data source and page size as input. It also initializes the current page to 0 and calculates the total number of records.
- Iterator Protocol: The __iter__ method returns the iterator object itself, and the __next__ method fetches the next page of records.
- Fetching Records: The _fetch_records method simulates retrieving records from the data source, while _get_total_records returns the total number of records in the data source.
- Using the Iterator: The for loop iterates over the pages of records, printing each page of 100 records.