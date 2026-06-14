import os
import requests
import base64
import re

SOURCE_URLS = [
    "https://sub22.aboshahr.co.uk:2087/sub22/6n7pqitdmuuconys"   # لینک خودت
]

OUTPUT_DIR = "configs"
ALL_CONFIGS_FILE = os.path.join(OUTPUT_DIR, "all_configs.txt")

def fetch_configs(url):
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            return []
        text = r.text
        # اگر base64 بود decode کن
        if re.match(r'^[A-Za-z0-9+/=]+$', text.strip()):
            try:
                text = base64.b64decode(text).decode('utf-8')
            except:
                pass
        lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith('#')]
        return lines
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_configs = []
    for url in SOURCE_URLS:
        print(f"Fetching {url}")
        cfgs = fetch_configs(url)
        all_configs.extend(cfgs)
        print(f"Found {len(cfgs)} configs")
    unique = list(dict.fromkeys(all_configs))
    with open(ALL_CONFIGS_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique))
    print(f"Saved {len(unique)} configs to {ALL_CONFIGS_FILE}")

if __name__ == "__main__":
    main()
