#!/usr/bin/python3
""" JSON & the json module revisited """
import json


def main():
    """ testing json.dump(obj, file) with indent option enabled:
        a value of 0 says - each value on its own line while a positive
        integer greater than 0 says the same with the additional
        spacing for indented structures
    """
    an_entry = {} # an empty dictionary
    an_entry['id'] = 256
    an_entry['title'] = 'Dive into history, 2009 edition'
    an_entry['tags'] = ('diveintohistory', 'docbook', 'html')
    an_entry['published'] = True
    an_entry['comments_link'] = None
    
    with open('basic_indented.json', mode='w', encoding='utf-8') as f:
        json.dump(an_entry, f, indent=2) 
        # space (indent) nested structures two sapces in

# call the function
main()
