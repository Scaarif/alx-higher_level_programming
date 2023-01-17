#!/usr/bin/python3
""" Takes in a URL as an argument and sends a request to the URL and
    displays the body of the response (decoded in utf-8)
    Note: manages urllib.error.HTTError exception...
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
