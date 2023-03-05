#!/usr/bin/env python3

import argparse
import json
import os
from pathlib import Path
from xml.etree import ElementTree
import unicodedata
from base64 import b64decode
from striprtf.striprtf import rtf_to_text

import tarfile


def write_json(obj, filename):
    with open(filename, "w") as f:
        f.write(json.dumps(obj, indent=4, ensure_ascii=False))


def pro6_xml_song_to_plain_slides(pro6_xml: str) -> list[str]:
    tree = ElementTree.fromstring(pro6_xml)
    strings = []
    # iterate slides in propresenter xml file
    for el in tree.findall(".//NSString"):
        # sanity check
        if el.attrib.get("rvXMLIvarName") != "RTFData":
            continue

        rtf = b64decode(el.text).decode("utf-8")
        # 1. rtf to plain text
        # 2. make sure the slide is unicode normalized
        # 3. remove long divider lines
        plain = rtf_to_text(rtf, errors="ignore")
        plain = unicodedata.normalize("NFKC", plain)
        plain = plain.replace("-----------------", "")

        # skip slides that say "Double-click to edit"
        if "Double-click" in plain:
            continue

        # skip if empty
        if plain.strip() == "":
            continue

        strings.append(plain)

    return strings


def songs_tgz_to_songs(songs_tgz) -> list:
    songs = []
    with tarfile.open(songs_tgz, mode="r") as tar:
        for filename in tar.getmembers():
            # apples shitty metadata files
            if "._" in filename.name:
                continue
            # only the correct files
            if not filename.name.endswith(".pro6"):
                continue

            pro6_xml = tar.extractfile(filename).read()
            slides = pro6_xml_song_to_plain_slides(pro6_xml)
            basename = Path(filename.name).stem
            song = {
                "title": unicodedata.normalize("NFKC", basename),
                "text": slides,
            }
            songs.append(song)

    return sorted(songs, key=lambda x: x["title"])


def pro6pl_to_playlists(pro6pl_filename, date_swaps) -> list:
    root = ElementTree.parse(pro6pl_filename).getroot()

    playlists = []

    for playlist in root.findall(".//RVPlaylistNode"):
        playlist_name = playlist.get("displayName")
        playlist_date = playlist.get("modifiedDate")
        if playlist_date in date_swaps:
            playlist_date = date_swaps[playlist_date]

        songs = []
        for song in playlist.findall("array/RVDocumentCue"):
            song_name = song.get("displayName")
            songs.append(unicodedata.normalize("NFKC", song_name))

        if len(songs) == 0:
            continue

        playlist = {
            "playlist_name": unicodedata.normalize("NFKC", playlist_name),
            "playlist_date": unicodedata.normalize("NFKC", playlist_date),
            "songs": songs,
        }
        playlists.append(playlist)

    return sorted(playlists, key=lambda x: x["playlist_date"])


def read_json(filename):
    with open(filename) as f:
        return json.load(f)


def main(pro6pl_filename, songs_tgz, date_swaps_json, outdir):
    os.makedirs(outdir, exist_ok=True)

    if date_swaps_json:
        date_swaps = read_json(date_swaps_json)
    else:
        date_swaps = {}

    playlists = pro6pl_to_playlists(pro6pl_filename, date_swaps)
    if len(playlists) == 0:
        print("WARN: you have no playlists")
    write_json(playlists, f"{outdir}/playlists.json")

    songs = songs_tgz_to_songs(songs_tgz)
    if len(songs) == 0:
        print("WARN: you have no songs")
    write_json(songs, f"{outdir}/songs.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Helper script to convert from the pro6 XML data formats to two json files: playlists.json and songs.json."
    )
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--playlist_pro6pl", required=True)
    parser.add_argument("--songs_tgz", required=True)
    parser.add_argument("--date-swaps", default=None)
    args = parser.parse_args()
    main(args.playlist_pro6pl, args.songs_tgz, args.date_swaps, args.outdir)
