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