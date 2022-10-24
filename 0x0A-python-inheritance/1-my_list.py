#!/usr/bin/python3
""" Defines a class that inherits from list """


class MyList(list):
    """ a class that inherits from list """
    def print_sorted(self):
        """ prints the list, sorted in ascending order """
        self.sort()  # call list.sort method
        print(self)  # print self (the instance of a list)
