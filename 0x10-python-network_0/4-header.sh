#!/bin/bash
# Takes in a URL, sends a GET request to the URL and displays the response body
curl -sfLX "GET" -H "X-School-User-Id: 98" "$1"
