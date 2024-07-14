
# AsyncIO 

AsyncIO is a library in Python that provides support for writing concurrent code using the async/await syntax. It is particularly useful for I/O-bound tasks, such as web scraping, where the program spends most of its time waiting for I/O operations to complete.


## Exercise

1. Open the file `LabFiles_Advance/06-concurrency/try_asyncio.py`.
2. Take a look at the code.

```python
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]


# Define an asynchronous function to fetch a URL


```
3. Implement the fetch_url function to fetch the URL and print the title of the page. by using the `async` and `await` keywords.

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

# Define an asynchronous function to fetch a URL
async def fetch_url(session, url):
    
    # Use the aiohttp library to fetch the URL
    # the `async with` statement is used to create a context manager
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(f"Title of {url}: {soup.title.string}")
```

4. Create an asynchronous function to fetch all URLs concurrently.

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

async def fetch_url(session, url):
    
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(f"Title of {url}: {soup.title.string}")

# Define an asynchronous function to fetch multiple URLs
async def main(urls):
    
    # Create a session object to manage connections, without having to create a new connection for each request
    # the `async with` statement is used to create a context manager
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        
        # Use `asyncio.gather` to run multiple tasks concurrently
        # `*tasks` is used to unpack the list of tasks into individual arguments
        await asyncio.gather(*tasks)



# Run the main function using asyncio
asyncio.run(main(urls))
```

3. Save file, run the script and observe the output.

```bash
python try_asyncio.py
```
