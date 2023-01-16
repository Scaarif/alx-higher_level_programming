#!/bin/bash
# Takes a URL as first argument and displays all HTTPS methods the server will accept
curl -sX "OPTIONS" "$1" | grep 'Allow' | cut -d ':' -f2
