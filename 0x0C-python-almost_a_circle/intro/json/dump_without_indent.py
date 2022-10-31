#!/usr/bin/python3
""" JSON & the json module revisited """
import json


def main():
    """ testing json.dump(obj, file) without the indent option
    everything ends up on the same line """
    an_entry = {} # an empty dictionary
    an_entry['id'] = 256
    an_entry['title'] = 'Dive into history, 2009 edition'
    an_entry['tags'] = ('diveintohistory', 'docbook', 'html')
    an_entry['published'] = True
    an_entry['comments_link'] = None
    
    with open('basic.json', mode='w', encoding='utf-8') as f:
        json.dump(an_entry, f)

# call the function
main()
