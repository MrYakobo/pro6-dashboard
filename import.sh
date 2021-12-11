#!/usr/bin/env bash

if [ ! -f "$1" ]; then
    echo "Supply the path to a tar.gz file that contains the songs from Propresenter"
    exit 1
fi

set -e

script_path="$PWD"
songs_archive="$(realpath "$1")"

pro6pl_file="$(realpath "$2")"

mkdir -p working_dir
cd working_dir
tar --skip-old-files -xzf "$songs_archive"

# find the unpacked pro6 files and convert them to txt
find . -type f -name '*.pro6' ! -name '._*' -print0 | xargs -0 "$script_path/pro6-to-txt/pro6-to-txt.py"

# do some sed action on those plain text files
find . -type f -name "*.txt" -print0 | xargs -0 sed -i 's/-----------------//g;/Double-click/d'

gen_json(){
    echo "["
    find . -name "*.txt" -print0 | while read -d $'\0' filename; do
        jq -n \
            --arg filename "$(basename -s .txt "$filename")" \
            --arg contents "$(cat "$filename")" \
            '{
                title: $filename,
                text: $contents
            }'
        echo ","
    done
}

out="songs.json"
echo "Now generating $out..."
gen_json > "$out"

# remove last comma
head -n -1 "$out" > /tmp/a && mv /tmp/a "$out"
echo "]" >> "$out"

echo "Done!"