#!/usr/bin/env python3

from sys import argv
import json
import xml.etree.ElementTree as ET

if len(argv) < 1:
    print("You must specify a .pro6pl file to convert to json.")
    exit()

root = ET.parse(argv[1]).getroot()

playlists = []

for playlist in root.findall(".//RVPlaylistNode"):
    playlist_name = playlist.get("displayName")
    playlist_date = playlist.get("modifiedDate")
    songs = []
    for song in playlist.findall("array/RVDocumentCue"):
        song_name = song.get("displayName")
        songs.append(song_name)

    if len(songs) == 0:
        continue

    playlist = {
        "playlist_name": playlist_name,
        "playlist_date": playlist_date,
        "songs": songs,
    }
    playlists.append(playlist)

print(json.dumps(playlists, indent=4, ensure_ascii=False))
