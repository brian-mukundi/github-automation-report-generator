import requests
from config import GITHUB_USERNAME, GITHUB_TOKEN


def fetch_github_data():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()

    return response.json()
