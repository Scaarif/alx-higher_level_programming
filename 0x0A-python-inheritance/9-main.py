#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
r = Rectangle(3, 5)
print(r)
print(r.area())
try:
    r = Rectangle(3.5, 5)
    print(r)
    print(r.area())
except Exception as e:
    print(e.__class__.__name__, e)