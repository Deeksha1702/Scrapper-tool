import requests

def fetch_article(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.content
