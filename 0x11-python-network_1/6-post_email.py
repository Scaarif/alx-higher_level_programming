#!/usr/bin/python3
""" Takes in a URL & email as arguments and sends a request to the URL with
    the email as a parameter and displays the body of the response
    (decoded in utf-8)
"""
import requests
import sys


if __name__ == "__main__":
    url = f'{sys.argv[1]}'
    data = {}
    data['email'] = sys.argv[2]
    res = requests.post(url, data=data)
    print(res.text)
