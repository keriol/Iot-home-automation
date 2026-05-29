#!/usr/bin/env python3
import subprocess
import sys

if len(sys.argv) < 2:
    print('Uso: plex_resume.py "One Piece"')
    sys.exit(1)

query = sys.argv[1]

search = subprocess.run(
    ["/config/plex_search.py", query],
    capture_output=True,
    text=True
)

print(search.stdout)

if search.returncode != 0:
    print(search.stderr)
    sys.exit(search.returncode)

play = subprocess.run(
    ["/config/plex_play_result.py", "1"],
    capture_output=True,
    text=True
)

print(play.stdout)

if play.returncode != 0:
    print(play.stderr)
    sys.exit(play.returncode)
