#!/usr/bin/python3
"""
    Adds all arguments to a Python list
    and then saves them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# add all arguments to a Python list, and then save them to a file
filename = 'add_item.json'
# load the existing contents of the list if file already exists
try:
    args = load_from_json_file(filename)
except Exception:
    args = []
# get the args (from cmd-line) to add to the list
if len(sys.argv) - 1:
    idx = 1
    while idx < len(sys.argv):
        args.append(sys.argv[idx])
        idx += 1
# save the args (object) into a json file, add_item.json
save_to_json_file(args, filename)
# read(load) the contents saved to json file
# print(load_from_json_file(filename)) - prints Python Object
# with open(filename, encoding='utf-8') as f:
# print(f.read())  # prints json object
