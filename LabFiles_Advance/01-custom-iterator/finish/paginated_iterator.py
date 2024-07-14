class PaginatedRecords:
    def __init__(self, data_source, page_size=100):
        self.data_source = data_source
        self.page_size = page_size
        self.current_page = 0
        self.total_records = self._get_total_records()
    
    def __iter__(self):
        return self
    
    # Implementing the __next__ method to return the next page of records
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