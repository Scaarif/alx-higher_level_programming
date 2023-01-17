#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using the urllib package
    and displays the  body of the response
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res)))
        print('\t- content: {}'.format(res))
        print('\t- utf8 content: {}'.format(res.decode("utf-8")))
