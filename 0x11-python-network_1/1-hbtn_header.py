#!/usr/bin/python3
""" Takes in a URL as argument and sends a request to the URL, displaying
    the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        res = response.info()
        print(res['X-Request-Id'])
