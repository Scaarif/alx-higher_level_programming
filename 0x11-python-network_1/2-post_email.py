#!/usr/bin/python3
""" Takes in a URL & email as arguments and sends a request to the URL with
    the email as a parameter and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request
import sys


url = f'{sys.argv[1]}'
data = {}
data['email'] = sys.argv[2]
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    res = response.decode('utf-8')
    print(res)
