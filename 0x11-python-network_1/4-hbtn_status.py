#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using requests package
    and displays the  body of the response
"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    # print the res, formatted (assuming its a dict)
    print('Body responses:', res.text)
    # for (key, value) in res.items():
    # print(f'\t- {key}: {value}')
