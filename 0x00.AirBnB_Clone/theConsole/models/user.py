#!/usr/bin/python3
""" Defines the class User, that inherits from class BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines the attributes/ methods of a User instance """
    # define (public) class attributes
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self):
        """ Initialize user objects """
        # initialize super class
        Base.__init__(self, *args, **args)
