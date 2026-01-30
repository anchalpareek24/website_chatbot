import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Request failed:", e)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["nav", "footer", "header", "script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    cleaned_text = " ".join(text.split())

    return cleaned_text if cleaned_text else None


