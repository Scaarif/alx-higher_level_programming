#!/usr/bin/python3
""" Defines the class City, that inherits from class BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the attributes/ methods of a City instance """
    # define (public) class attributes
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user objects """
        # initialize super class
        BaseModel.__init__(self, *args, **kwargs)
