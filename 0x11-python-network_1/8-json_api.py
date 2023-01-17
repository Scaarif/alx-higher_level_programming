#!/usr/bin/python3
""" Takes in a letter as an argument and sends a POST request to
    'http://0.0.0.0:5000/search_user with the letter as parameter
    Requirements: the letter must be sent in the variable 'q'
                  if no argument is given, set q=""
                  if the respomse body is properly JSON formatted
                  (and not empty),
                    display the id and name like [<id>] <name>
                  else:
                    diplay 'Not a valid JSON' if the JSON is invalid
                    display 'No result' if the JSON is empty
    displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    if res.status_code == 204:  # no content (empty)
        print('No result')
    else:
        try:
            val = res.json()
            print('[{}] {}'.format(val.get('id'), val.get('name')))
        except requests.exceptions.JSONDecodeError:
            print('Not a valid JSON')
