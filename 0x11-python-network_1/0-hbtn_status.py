#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using the urllib package
    and displays the  body of the response
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        res = response.read()
        # print the res, formatted (assuming its a dict)
        print('Body responses:')
        print(f'\t- type: {type(res)}')
        print(f'\t- content: {res}')
        print(f'\t- utf-8 content: {res.decode("utf-8")}')
