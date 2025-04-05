import requests
from bs4 import BeautifulSoup

def fetch_and_clean_html(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Return raw HTML (not plain text)
    body = soup.body
    return str(body) if body else soup.prettify()