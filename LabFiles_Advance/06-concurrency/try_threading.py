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