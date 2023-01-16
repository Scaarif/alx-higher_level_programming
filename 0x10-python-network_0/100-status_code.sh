#!/bin/bash
# Takes in a URL passed as an argument, sends a request to the URL and displays only the status code of the response
curl -w '%{http_code}\n' "$1"
