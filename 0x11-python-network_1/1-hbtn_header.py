#!/usr/bin/python3
""" Takes in a URL as argument and sends a request to the URL, displaying
    the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


req = urllib.request.Request(f'{sys.argv[1]}')
with urllib.request.urlopen(req) as response:
    res = response.info()  # get the headers from the response
    print(res['X-Request-Id'])  # info() returns a dict
