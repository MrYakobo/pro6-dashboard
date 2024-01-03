#!/usr/bin/env python3
# to be ran on a computer with Propresenter 6 files

import argparse
import dataclasses
import json
import os
import unicodedata
from base64 import b64decode
from dataclasses import dataclass
from glob import glob
from pathlib import Path
from typing import NewType
from xml.etree import ElementTree

from striprtf.striprtf import rtf_to_text

SongTitle = NewType("SongTitle", str)
Slide = NewType("Slide", str)


def slides_from_pro6(pro6_filename: str) -> list[Slide]:
    with open(pro6_filename, "r") as f:
        tree = ElementTree.fromstring(f.read())

    slides = []
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

        slides.append(Slide(plain))

    return slides


@dataclass
class Song:
    title: SongTitle
    text: list[Slide]

    def __lt__(self, other):
        return self.title < other.title

    @staticmethod
    def from_pro6(pro6_filename: str) -> "Song":
        slides = slides_from_pro6(pro6_filename)
        basename = Path(pro6_filename).stem
        normalized_basename = unicodedata.normalize("NFKC", basename)
        return Song(title=normalized_basename, text=slides)


@dataclass
class Playlist:
    playlist_name: str
    playlist_date: str
    songs: list[SongTitle]

    def __lt__(self, other):
        return self.playlist_date < other.playlist_date

    @staticmethod
    def playlists_from_pro6pl(pro6pl_filename: str) -> list["Playlist"]:
        root = ElementTree.parse(pro6pl_filename).getroot()

        playlists = []

        for playlist in root.findall(".//RVPlaylistNode"):
            playlist_name = playlist.get("displayName")
            playlist_date = playlist.get("modifiedDate")

            songs = []
            for song in playlist.findall("array/RVDocumentCue"):
                song_name = song.get("displayName")
                normalized_song_name = unicodedata.normalize("NFKC", song_name)
                songs.append(normalized_song_name)

            if len(songs) == 0:
                print(
                    f'INFO: skipping playlist "{playlist_name}" due to it not containing any songs'
                )
                continue

            playlist = Playlist(
                playlist_name=unicodedata.normalize("NFKC", playlist_name),
                playlist_date=unicodedata.normalize("NFKC", playlist_date),
                songs=songs,
            )
            playlists.append(playlist)

        return sorted(playlists)


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def write_json(obj, filename):
    with open(filename, "w") as f:
        f.write(json.dumps(obj, indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder))


def generate_jsonfiles(pro6pl_filename, songs_dir, outdir):
    os.makedirs(outdir, exist_ok=True)

    playlists = Playlist.playlists_from_pro6pl(pro6pl_filename)
    if len(playlists) == 0:
        print("WARN: you have no playlists")

    write_json(playlists, f"{outdir}/playlists.json")

    song_filenames = glob(f"{songs_dir}/**/*.pro6", recursive=True)

    # "._": apple shitty metadata files
    songs = [
        Song.from_pro6(filename) for filename in song_filenames if "._" not in filename
    ]
    if len(songs) == 0:
        print("WARN: you have no songs")

    write_json(songs, f"{outdir}/songs.json")


def main():
    parser = argparse.ArgumentParser(
        "Helper script to convert from the pro6 XML data formats to two json files: playlists.json and songs.json."
    )
    parser.add_argument("--outdir", default="out")
    parser.add_argument(
        "--playlist_pro6pl",
        default=os.path.expanduser(
            "~/Library/Application Support/RenewedVision/ProPresenter6/Playlists/ProPresenter6.pro6pl"
        ),
    )
    parser.add_argument(
        "--songs_dir",
        default=os.path.expanduser("~/Documents/ProPresenter6"),
    )
    args = parser.parse_args()
    generate_jsonfiles(args.playlist_pro6pl, args.songs_dir, args.outdir)


if __name__ == "__main__":
    main()
