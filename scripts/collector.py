import os
import requests
import base64
import re
from datetime import datetime

SOURCE_URLS = [
    "https://sub22.aboshahr.co.uk:2087/sub22/6n7pqitdmuuconys"  # لینک خودت رو اینجا عوض کن
]
OUTPUT_DIR = "configs"
ALL_CONFIGS_FILE = os.path.join(OUTPUT_DIR, "all_configs.txt")

def fetch_configs_from_url(url):
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return []
        content = response.text
        if re.match(r'^[A-Za-z0-9+/=]+$', content.strip()):
            try:
                content = base64.b64decode(content).decode('utf-8')
            except:
                pass
        lines = content.splitlines()
        configs = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
        return configs
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_configs = []
    for url in SOURCE_URLS:
        print(f"Fetching {url}")
        configs = fetch_configs_from_url(url)
        all_configs.extend(configs)
    unique_configs = list(dict.fromkeys(all_configs))
    with open(ALL_CONFIGS_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_configs))
    print(f"Saved {len(unique_configs)} configs")

if __name__ == "__main__":
    main()
