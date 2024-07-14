
# Multiprocessing 

Multiprocessing is a module in Python that allows you to create processes, which are separate instances of the Python interpreter. This is useful for web scraping because it allows you to run multiple instances of your web scraping script simultaneously, which can significantly speed up the process.

## Exercise

1. Open the file `LabFiles_Advance/06-concurrency/try_multiprocessing.py`.
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


```

2. Implement the following steps:
    - Create a list of threads.
    - Start each thread.
    - Wait for all threads to finish.

```python
import multiprocessing
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

# Create a list of processes in the same way as threads
if __name__ == '__main__':

    processes = []
    for url in urls:
        
        # Create a process object, and start it
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Finished scraping all URLs.")
```

3. Save file, run the script and observe the output.


```bash
python try_multiprocessing.py
```
