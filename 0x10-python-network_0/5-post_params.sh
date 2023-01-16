#!/bin/bash
# Takes in a URL, sends a POST request to the URL and displays the response body
curl -sfLd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
