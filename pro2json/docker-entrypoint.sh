#!/usr/bin/env bash

set -eu

export TZ=Europe/Stockholm

while true; do
  # Get the current time and calculate the number of seconds until target_time
  current_time=$(date +%s)
  target_time=$(date -d 'today 13:34:00' +%s)
  sleep_time=$((target_time - current_time))

  echo "curr: $current_time; target_time: $target_time; sleep_time: $sleep_time"

  if [[ $sleep_time < 0 ]]; then
	  # if we're past the trigger time today, wait until tomorrow
	  echo "we're past the trigger time today, wait until tomorrow"
	  sleep 23h
	  continue
  fi

  # Wait until target_time to execute the command
  sleep $sleep_time
  echo "finished sleeping"

  # Execute the command
  /app/pro2json.py \
    --outdir /outdir \
    --songs_tgz /indir/songs.tgz \
    --playlist_pro6pl /indir/ProPresenter6.pro6pl
done
