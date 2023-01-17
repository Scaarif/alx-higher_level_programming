#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using requests package
    and displays the  body of the response
"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    # print the res, formatted (assuming its a dict)
    print('Body response:')
    print(f'\t- type: {type(res.text)}')
    print(f'\t- content: {res.text}')
