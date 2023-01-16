#!/bin/bash
# Takes in a URL and filename as rguments, sends a POST request to URL and displays the body of the response
curl -sfd @"$2" "$1"
