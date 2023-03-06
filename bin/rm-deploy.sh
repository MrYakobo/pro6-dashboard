#!/usr/bin/env bash

set -exu

COMMITISH="$1"
ssh pi "rm -rf $SERVER_COLON_PATH/$COMMITISH"