import requests

def fetch_json(url: str) -> str:
    """Fetch plain text from the given URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

