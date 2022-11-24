#!/usr/bin/python3
""" Defines the class Review, that inherits from class BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the attributes/ methods of a Review instance """
    # define (public) class attributes
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initialize user objects """
        # initialize super class
        BaseModel.__init__(self, *args, **kwargs)
