#!/usr/bin/python3
""" Defines the class Amenity, that inherits from class BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Defines the attributes/ methods of a Amenity instance """
    # define (public) class attributes
    name = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user objects """
        # initialize super class
        BaseModel.__init__(self, *args, **kwargs)
