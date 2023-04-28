#!/usr/bin/env bash

set -exu

COMMITISH="$1"
# if you want to deploy main, supply HEAD as commitish
DEPLOY_PATH="$COMMITISH"

if [[ "$COMMITISH" = "main" ]]; then
    # deploy to root
    DEPLOY_PATH=""
fi

tmpdir=$(mktemp -d)

cleanup(){
    rm -rf "$tmpdir"
}

trap cleanup EXIT

# deploy a specific tag to the server

# first, copy the working tree to a temporary directory
cp -r "$(git rev-parse --show-toplevel)"/ "$tmpdir"
(
    cd "$tmpdir/web"

    # then, checkout the commitish
    git checkout -f "$COMMITISH"

    # build the site (clean install)
    npm ci
    npm run build

    # copy the data files into dist
    cp -r data dist

    ls -l dist

    # scp the dist folder to the server
    scp -r dist/* "$SERVER_COLON_PATH/$DEPLOY_PATH"
)