#!/usr/bin/env bash

set -exu

COMMITISH="$1"
HOST="$(echo "$SERVER_COLON_PATH" | cut -d: -f1)"
PATH="$(echo "$SERVER_COLON_PATH" | cut -d: -f2-)"

ssh "$HOST" "rm -rf $PATH/$COMMITISH"