import asyncio
import aiohttp
from bs4 import BeautifulSoup

# Define an asynchronous function to fetch a URL
async def fetch_url(session, url):
    
    # Use the aiohttp library to fetch the URL
    # the `async with` statement is used to create a context manager
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(f"Title of {url}: {soup.title.string}")

# Define an asynchronous function to fetch multiple URLs
async def main(urls):
    
    # Create a session object to manage connections
    # the `async with` statement is used to create a context manager
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        
        # Use `asyncio.gather` to run multiple tasks concurrently
        # `*tasks` is used to unpack the list of tasks into individual arguments
        await asyncio.gather(*tasks)

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

# Run the main function using asyncio
asyncio.run(main(urls))