import os
import re
import json
import urllib.request
from bs4 import BeautifulSoup

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "scraped_theses", "manifest.json")
BASE_DIR = os.path.dirname(MANIFEST_PATH)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def sanitize(val):
    clean = re.sub(r'[\\/*?:"<>|]', "", val)
    return clean[:60].strip()

def enrich():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    for item in manifest:
        url = item.get("url")
        print(f"Fetching metadata for {url}...")
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
            soup = BeautifulSoup(html, "html.parser")
            
            # Extract citation or DC tags
            title_tag = soup.find("meta", attrs={"name": "citation_title"}) or soup.find("meta", attrs={"name": "DC.title"})
            author_tag = soup.find("meta", attrs={"name": "citation_author"}) or soup.find("meta", attrs={"name": "DC.creator"})
            date_tag = soup.find("meta", attrs={"name": "citation_publication_date"}) or soup.find("meta", attrs={"name": "DCTERMS.issued"})
            abstract_tag = soup.find("meta", attrs={"name": "DCTERMS.abstract"})
            
            if title_tag and title_tag.get("content"):
                item["title"] = title_tag["content"].strip()
            elif soup.find("h2"):
                item["title"] = soup.find("h2").get_text(strip=True)

            if author_tag and author_tag.get("content"):
                item["author"] = author_tag["content"].strip()
                
            if date_tag and date_tag.get("content"):
                item["date"] = date_tag["content"].strip()
                
            if abstract_tag and abstract_tag.get("content"):
                item["abstract"] = abstract_tag["content"].strip()[:400] + "..."

            # Rename local file if exists
            old_filename = item.get("local_filename")
            if old_filename:
                old_path = os.path.join(BASE_DIR, old_filename)
                if os.path.exists(old_path):
                    handle_id = item["handle"].split("/")[-1]
                    clean_author = sanitize(item.get("author", "Autor")).replace(" ", "_")
                    clean_title = sanitize(item.get("title", "Tesis")).replace(" ", "_")
                    new_filename = f"TESIS_UNI_{handle_id}_{clean_author}_{clean_title}.pdf"
                    new_path = os.path.join(BASE_DIR, new_filename)
                    if old_path != new_path:
                        try:
                            os.rename(old_path, new_path)
                            item["local_filename"] = new_filename
                            item["local_path"] = new_path
                            print(f"  Renamed to: {new_filename}")
                        except Exception as e:
                            print(f"  Error renaming: {e}")
        except Exception as e:
            print(f"Error enriching {url}: {e}")

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print("Manifest successfully enriched!")

if __name__ == "__main__":
    enrich()
