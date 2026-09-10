import os
import re
import json
import time
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
BASE_URL = "https://cybertesis.uni.edu.pe"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "scraped_theses")
MANIFEST_PATH = os.path.join(OUTPUT_DIR, "manifest.json")

SEARCH_QUERIES = [
    "voladura minera subterránea",
    "geomecánica Barton Q sostenimiento",
    "Holmberg perforación voladura",
    "vibraciones voladura campo cercano",
    "machine learning minería fragmentación",
    "taladros largos subniveles",
    "ventilación minera subterránea"
]

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_handles_from_search(query, max_results=10):
    encoded_query = urllib.parse.quote_plus(query)
    search_url = f"{BASE_URL}/simple-search?query={encoded_query}&rpp={max_results}&sort_by=score&order=desc"
    html = fetch_url(search_url)
    if not html:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    handles = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "/handle/20.500.14076/" in href:
            clean_href = href.split("?")[0]
            if clean_href not in handles and not clean_href.endswith("browse") and not clean_href.endswith("submit"):
                handles.append(clean_href)
    return handles

def get_thesis_metadata_and_pdf(handle_path):
    url = f"{BASE_URL}{handle_path}"
    html = fetch_url(url)
    if not html:
        return None
    
    soup = BeautifulSoup(html, "html.parser")
    
    title_elem = soup.find("h2", class_="page-header") or soup.find("h2")
    title = title_elem.get_text(strip=True) if title_elem else "Sin Titulo"
    
    author_elem = soup.find("span", class_="author") or soup.find("div", class_="simple-item-view-authors")
    author = author_elem.get_text(strip=True) if author_elem else "Desconocido"
    
    date_elem = soup.find("div", class_="simple-item-view-date")
    date = date_elem.get_text(strip=True) if date_elem else "2024"
    
    # Find PDF bitstream link
    pdf_url = None
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "/bitstream/handle/20.500.14076/" in href and href.lower().endswith(".pdf"):
            pdf_url = f"{BASE_URL}{href}" if not href.startswith("http") else href
            break
            
    if not pdf_url:
        # Check any bitstream link
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "/bitstream/" in href:
                pdf_url = f"{BASE_URL}{href}" if not href.startswith("http") else href
                break

    return {
        "handle": handle_path,
        "url": url,
        "title": title,
        "author": author,
        "date": date,
        "pdf_url": pdf_url
    }

def download_file(url, target_path):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as response, open(target_path, "wb") as out_file:
            out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def sanitize_filename(name):
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean[:80].strip()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    manifest = []
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                manifest = json.load(f)
        except Exception:
            manifest = []
            
    existing_handles = {item.get("handle") for item in manifest}
    
    print(f"Starting thesis scraping from Cybertesis UNI...")
    all_handles = set()
    for q in SEARCH_QUERIES:
        print(f"Searching: '{q}'...")
        handles = extract_handles_from_search(q, max_results=10)
        print(f"  Found {len(handles)} handles.")
        for h in handles:
            all_handles.add(h)
        time.sleep(1)

    print(f"\nTotal unique thesis handles discovered: {len(all_handles)}")
    
    new_downloads = 0
    for h in all_handles:
        if h in existing_handles:
            print(f"Skipping already recorded handle: {h}")
            continue
            
        print(f"\nProcessing {h}...")
        meta = get_thesis_metadata_and_pdf(h)
        if not meta:
            continue
            
        print(f"  Title: {meta['title'][:60]}...")
        print(f"  Author: {meta['author']}")
        print(f"  PDF URL: {meta['pdf_url']}")
        
        if meta['pdf_url']:
            handle_id = h.split("/")[-1]
            safe_title = sanitize_filename(meta['title'])
            filename = f"TESIS_UNI_{handle_id}_{safe_title}.pdf"
            pdf_path = os.path.join(OUTPUT_DIR, filename)
            
            print(f"  Downloading to {filename}...")
            if download_file(meta['pdf_url'], pdf_path):
                file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"  Downloaded successfully ({file_size_mb:.2f} MB)")
                meta["local_filename"] = filename
                meta["local_path"] = pdf_path
                meta["size_mb"] = round(file_size_mb, 2)
                manifest.append(meta)
                existing_handles.add(h)
                new_downloads += 1
                
                # Save progress
                with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
                    json.dump(manifest, f, indent=2, ensure_ascii=False)
            else:
                print(f"  Failed to download PDF.")
        time.sleep(1)
        
        # Stop if we have downloaded enough
        if len(manifest) >= 25:
            print("\nReached target of 25+ theses in manifest!")
            break

    print(f"\nFinished scraping session. Total theses in manifest: {len(manifest)}")

if __name__ == "__main__":
    main()
