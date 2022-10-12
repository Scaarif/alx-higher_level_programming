#!/usr/bin/python3
""" Creating a class Node & another, SinglyLinkedList """


class Node:
    """ creates an a class, Node, with 2 private attributes """
    def __init__(self, data, next_node=None):
        """ Initialize the instance """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ data getter method """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter method with type and value enforcement
        args:
            value: the data parameter in __init__
        """
        # check that data is an int and raise an exception if not
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter for the next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter method for the next_node attribute """
        # check that next_node is None or a Node (type)
        if value and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """
    def __init__(self):
        """ Initialize class instance """
        self.__head = None  # instantiate a Node

    def __repr__(self):
        """ represent the linked list as a printable object, a
        node a line """
        curr = self.__head
        lkd_list = ""
        while curr:
            # concatenate nodes to the list representation
            lkd_list += "{:d}".format(curr.data)
            curr = curr.next_node
            # if we still have a node to concatenate, add a new line
            if curr:
                lkd_list += "\n"
        return lkd_list

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position
        in the list (increasing order)
        args:
            value: a node to insert (with data & next_node)
        """
        # update head (here) - list's ordered (ascending) by data
        if self.__head is None:
            # list is currently empty, insert at the beginning
            new = Node(value)
            # new.data = value
            # new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            # insert at the head & update head
            new = Node(value)
            # new.data = value
            new.next_node = self.__head  # call the setter
            self.__head = new  # update __head
        else:
            # list not empty & insert not @ head - search for insert position
            pos = self.__head
            while (pos and pos.data < value):  # stop at pos.next_node?
                before = pos
                pos = pos.next_node
            # new Node should be inserted after this node (pos)
            temp = before.next_node
            new = Node(value)
            # new.data = value
            new.next_node = temp  # call the setter
            before.next_node = new   # call the setter
