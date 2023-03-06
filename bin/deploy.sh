#!/usr/bin/env bash

set -exu

COMMITISH="$1"

tmpdir=$(mktemp -d)

cleanup(){
    rm -rf "$tmpdir"
}

trap cleanup EXIT

# deploy a specific tag to the raspberry pi

# first, copy the working tree to a temporary directory
cp -r "$(git rev-parse --show-toplevel)"/ "$tmpdir"
cd "$tmpdir/web"

# then, checkout the commitish
git checkout "$COMMITISH"

# build the site (clean install)
npm ci
npm run build

# copy the data files into dist
cp -r data dist

ls -l

# scp the dist to the raspberry pi
scp -r dist "$SERVER_COLON_PATH/$COMMITISH"