#!/usr/bin/bash
# Takes in a URL, sends a request to the URL and displays the size of the response body
curl -sfLI "$1" | grep 'Content-Length' | cut -d " " -f2
