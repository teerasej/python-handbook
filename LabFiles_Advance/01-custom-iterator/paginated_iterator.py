class PaginatedRecords:
    def __init__(self, data_source, page_size=100):
        self.data_source = data_source
        self.page_size = page_size
        self.current_page = 0
        self.total_records = self._get_total_records()
    
    def __iter__(self):
        return self
    
    # Implementing the __next__ method to return the next page of records
        
    
    def _get_total_records(self):
        # Simulate getting total record count from the data source
        return len(self.data_source)
    
    def _fetch_records(self, start, end):
        # Simulate fetching records from the data source
        return self.data_source[start:end]

# Simulate a large dataset
data_source = [f"Record {i}" for i in range(1000)]

# Using the custom iterator for paginated records

for page in paginated_records:
    print(page)  # Output: Pages of 100 records each