#!/usr/bin/python3
"""Module to find the max integer in a list
"""
def max_integer(list=[]):
 """Function to find and return the max integer in a list of integers
 If the list is empty, the function returns None
 """
 if len(list) == 0:
     return None
 result = list[0]
 i = 1
 while i < len(list):
    if list[i] > result:
        result = list[i]
    i += 1
 return result


if __name__ == "__main__":
    print(max_integer([5,4,6,8,1,3]))
    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))
