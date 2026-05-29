#!/usr/bin/env python3
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HA_URL = "http://127.0.0.1:8123"
PLEX_URL = "http://PLEX_SERVER_HOST:32400"
HA_TOKEN_FILE = "/config/HA_TOKEN_FILE"
PLEX_TOKEN_FILE = "/config/PLEX_TOKEN_FILE"
RESULTS_FILE = "/config/plex_search_results.json"
PLAYER_ENTITY = "media_player.plex_plex_for_android_tv_bravia_vh2"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def pick_episode_for_show(show_rating_key, plex_token):
    url = (
        f"{PLEX_URL}/library/metadata/{show_rating_key}/allLeaves"
        f"?X-Plex-Token={urllib.parse.quote(plex_token)}"
    )

    with urllib.request.urlopen(url, timeout=15) as response:
        root = ET.fromstring(response.read())

    episodes = [item for item in root if item.attrib.get("type") == "episode"]

    partial = [
        ep for ep in episodes
        if int(ep.attrib.get("viewOffset", "0")) > 0 and ep.attrib.get("viewCount") != "1"
    ]

    if partial:
        return partial[0]

    unwatched = [
        ep for ep in episodes
        if ep.attrib.get("viewCount") != "1"
    ]

    if unwatched:
        return unwatched[0]

    return episodes[0] if episodes else None

def call_ha_play(media_content_id, media_content_type):
    ha_token = read_file(HA_TOKEN_FILE)

    payload = {
        "entity_id": PLAYER_ENTITY,
        "media_content_id": media_content_id,
        "media_content_type": media_content_type
    }

    req = urllib.request.Request(
        f"{HA_URL}/api/services/media_player/play_media",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {ha_token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=10) as response:
        response.read()

def main():
    if len(sys.argv) < 2:
        print("Uso: plex_play_result.py 1")
        sys.exit(1)

    index = int(sys.argv[1]) - 1

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        results = json.load(f)

    if index < 0 or index >= len(results):
        print(f"Risultato {index + 1} non valido")
        sys.exit(1)

    item = results[index]
    plex_token = read_file(PLEX_TOKEN_FILE)

    if item["type"] == "show":
        episode = pick_episode_for_show(item["ratingKey"], plex_token)

        if episode is None:
            print(f"Nessun episodio trovato per {item['title']}")
            sys.exit(1)

        episode_key = episode.attrib["ratingKey"]
        episode_title = episode.attrib.get("title", "")
        season = episode.attrib.get("parentIndex", "?")
        episode_number = episode.attrib.get("index", "?")

        media_content_id = item["media_content_id"].rsplit("/", 1)[0] + f"/{episode_key}"
        media_content_type = "EPISODE"

        call_ha_play(media_content_id, media_content_type)
        print(f"Avvio: {item['title']} S{season}E{episode_number} - {episode_title}")
        return

    call_ha_play(item["media_content_id"], item["media_content_type"])
    print(f"Avvio: {item['title']} - {item['library']}")

if __name__ == "__main__":
    main()
