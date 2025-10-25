import os
from bs4 import BeautifulSoup
import json

# Set the path manually
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # reader folder
nav_path = os.path.join(BASE_DIR, 'static', 'chapters', 'nav.xhtml')
json_path = os.path.join(BASE_DIR, 'static', 'chapters', 'chapters.json')

chapters = []
with open(nav_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    for li in soup.find_all('li'):
        a = li.find('a')
        if a:
            href = a['href']
            text = a.get_text(strip=True)
            chap_number = int(href.replace('chap_', '').replace('.xhtml',''))
            chapters.append({'number': chap_number, 'title': text, 'href': href})

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print(f"Saved {len(chapters)} chapters to {json_path}")
