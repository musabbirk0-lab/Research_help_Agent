import requests
from pathlib import Path

DOWNLOAD_DIR = Path("./data/pdfs")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

def download_pdf(url: str) -> str:
    """Download a PDF and return local path."""
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    fname = url.split("/")[-1].split("?")[0] or "doc.pdf"
    path = DOWNLOAD_DIR / fname
    with open(path, "wb") as f:
        f.write(r.content)
    return str(path)

if __name__ == "__main__":
    # tiny test
    test_url = "https://arxiv.org/pdf/2306.03672.pdf"
    print(download_pdf(test_url))
