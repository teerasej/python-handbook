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