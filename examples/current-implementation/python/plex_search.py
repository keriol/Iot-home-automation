#!/usr/bin/env python3
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape

PLEX_URL = "http://PLEX_SERVER_HOST:32400"
SERVER_ID = "0ac36193628143fe7cb3bff16aab516e1be5e2f1"
TOKEN_FILE = "/config/PLEX_TOKEN_FILE"
OUT_FILE = "/config/plex_search_results.json"

LIBRARY_PRIORITY = {
    "Anime": 1,
    "Programmi TV": 2,
    "Film": 3,
    "Film VM": 4,
}

def get_token():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def main():
    if len(sys.argv) < 2:
        print("Uso: plex_search.py \"One Piece\"")
        sys.exit(1)

    query = sys.argv[1]
    token = get_token()

    url = f"{PLEX_URL}/search?query={urllib.parse.quote(query)}&X-Plex-Token={urllib.parse.quote(token)}"

    with urllib.request.urlopen(url, timeout=10) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)

    results = []
    seen = set()

    for item in root:
        item_type = item.attrib.get("type")
        if item_type not in ("show", "movie"):
            continue

        rating_key = item.attrib.get("ratingKey")
        title = unescape(item.attrib.get("title", ""))
        library = item.attrib.get("librarySectionTitle", "")
        year = item.attrib.get("year", "")
        key = f"{item_type}:{rating_key}"

        if not rating_key or key in seen:
            continue

        seen.add(key)

        results.append({
            "title": title,
            "library": library,
            "type": item_type,
            "year": year,
            "ratingKey": rating_key,
            "media_content_id": f"plex://{SERVER_ID}/{rating_key}",
            "media_content_type": "EPISODE" if item_type == "show" else "movie"
        })

    results.sort(key=lambda r: (
        0 if r["title"].lower() == query.lower() else 1,
        LIBRARY_PRIORITY.get(r["library"], 99),
        r["title"]
    ))

    results = results[:5]

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    if not results:
        print(f"Nessun risultato trovato per: {query}")
        return

    print(f"Risultati Plex per '{query}':")
    for i, r in enumerate(results, start=1):
        year = f" ({r['year']})" if r["year"] else ""
        kind = "Serie" if r["type"] == "show" else "Film"
        print(f"{i}. {r['title']}{year} - {r['library']} - {kind}")

if __name__ == "__main__":
    main()
