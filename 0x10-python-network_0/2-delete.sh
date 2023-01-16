#!/bin/bash
# Takes a URL as first argument, sends a DELETE request to the URL and displays the body of the response
curl -sX "DELETE" "$1"
