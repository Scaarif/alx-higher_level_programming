#!/usr/bin/python3
""" Defines a function that returns the dictionary description
with simple data structure(list, dictionary, string, integer
& boolean) for JSON serialization of an object """
# import json


def class_to_json(obj):
    """ serializes serializable bits of a Python object and returns
    a dictionary description with simple data structure for JSON """
    class_dict = {}
    serializable = [list, str, dict, int, bool]
    # try to serialize the attributes of an object
    attr_list = dir(obj)
    # check if class_Name is defined
    if attr_list[0][-6:] == '__name':
        class_dict[attr_list[0]] = getattr(obj, attr_list[0])
    start = attr_list.index('__weakref__') + 1  # get the index of __weakref__
    # print(attr_list[start:])
    while start < len(attr_list):
        error = 1
        # try:
        val = getattr(obj, attr_list[start])
        # json.dumps(val)
        if type(val) in serializable:
            error = 0
        # if not serializable, pass
        # except Exception:
        # pass  # do nothing
        # add the serialized object to a dictionary object
        # as value with the object name as key
        if not error:
            attr = attr_list[start]
            # print("attr:", attr)
            class_dict[attr] = val
        start += 1
    return class_dict
