#!/usr/bin/python3
""" Defines a class Student that defines a student """


class Student(object):
    """ create a class Student """
    def __init__(self, first_name, last_name, age):
        """ initialize the class' instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ serializes serializable bits of the object(self) and returns
        a dictionary description with simple data structure for JSON """
        class_dict = {}
        serializable = [list, str, dict, int, bool]
        # try to serialize the attributes of an object
        attr_list = dir(self)
        # check if class_Name is defined
        if attr_list[0][-6:] == '__name':
            class_dict[attr_list[0]] = getattr(self, attr_list[0])
        # get the index of __weakref__
        start = attr_list.index('__weakref__') + 1
        while start < len(attr_list):
            val = getattr(self, attr_list[start])
            if type(val) in serializable:
                # add the serialized object to a dictionary object
                # as value with the object name as key if serializable
                attr = attr_list[start]
                # print("attr:", attr)
                class_dict[attr] = val
            start += 1
        return class_dict
