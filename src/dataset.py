import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = "https://exasasmple.com"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and print all titles (assuming they are in <h1> tags)
    titles = soup.find_all("h1")
    for title in titles:
        print(title.get_text())
else:
    print(f"Failed to retrieve data: {response.status_code}")
