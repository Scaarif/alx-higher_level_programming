#!/usr/bin/python3
""" Takes in a URL as argument and sends a request to the URL, displaying
    the value of the X-Request-Id variable found in the header of the response
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
