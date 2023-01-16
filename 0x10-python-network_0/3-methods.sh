#!/bin/bash
# Takes a URL as first argument and displays all HTTPS methods the server will accept
curl -sIX "OPTIONS" "$1" | grep 'Allow' | cut -d ' ' -f 2-
