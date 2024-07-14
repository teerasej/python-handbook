
# Basic Threading

Threading is a way to run multiple tasks concurrently within a single process. In Python, the `threading` module provides a simple way to create and manage threads. This module allows you to run multiple functions at the same time, which can be useful for tasks like web scraping, downloading files, or processing data.

## Exercise

1. Open the file `LabFiles_Advance/06-concurrency/try_threading.py`.
2. Take a look at the code.

```python
import threading
import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Title of {url}: {soup.title.string}")

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

# Create a list of threads


print("Finished scraping all URLs.")
```

2. Implement the following steps:
    - Create a list of threads.
    - Start each thread.
    - Wait for all threads to finish.

```python
import threading
import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Title of {url}: {soup.title.string}")

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

# Create a list of threads
threads = []
for url in urls:
    
    # Create a thread that will run the `fetch_url` function. 
    # The `args` parameter is used to pass arguments to the function.
    thread = threading.Thread(target=fetch_url, args=(url,))
    
    # Add the thread to the list
    threads.append(thread)
    
    # Start the thread
    thread.start()

# This will wait for all threads to finish
for thread in threads:
    # `thread.join()` will block the main thread until the thread finishes
    thread.join()

print("Finished scraping all URLs.")
```

3. Run the script and observe the output.

```bash
python try_threading.py
```

> Note: You might notice there is a 'pycache' folder created after running the script. This is a cache folder created by Python to store compiled bytecode files. You can safely ignore this folder.
