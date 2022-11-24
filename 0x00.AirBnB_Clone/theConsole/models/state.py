#!/usr/bin/python3
""" Defines the class State, that inherits from class BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """ Defines the attributes/ methods of a State instance """
    # define (public) class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user objects """
        # initialize super class
        BaseModel.__init__(self, *args, **kwargs)
