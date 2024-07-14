import asyncio
import aiohttp
from bs4 import BeautifulSoup

urls = [
    'https://nextflow.in.th',
    'https://learn.nextflow.in.th',
]

# Define an asynchronous function to fetch a URL