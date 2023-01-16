#!/bin/bash
# Takes in a URL, sends a request to the URL and displays the size of the response body
curl -s "$1" | wc -c
