#!/usr/bin/python3
""" Defines a function adds a new attribute to an object if its possible  """


def add_attribute(obj, name, value):
    """ adds an attribute to a class if possible  """
    # check if __slots__ is defined
    if '__slots__' in dir(obj):
        # if defined, check that the name provide is in slots
        if name not in dir(obj):
            raise TypeError('can\'t add new attribute')
    else:
        # check that the attribute doesn't already exist
        exists = getattr(obj, '__doc__', None)
        # if not, add the attribute
        if exists is None:
            setattr(obj, name, value)
        else:
            raise TypeError('can\'t add new attribute')


if __name__ == "__main__":
    class Test():
        __slots__ = ["first_name"]
        pass
    try:
        a = Test()
        add_attribute(a, 'hbtn', 'Holberton')
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
