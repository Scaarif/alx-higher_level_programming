#!/usr/bin/python3
""" Defines the class Place, that inherits from class BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Defines the attributes/ methods of a Place instance """
    # define (public) class attributes
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of strings(Amenity.id)

    def __init__(self, *args, **kwargs):
        """ Initialize user objects """
        # initialize super class
        BaseModel.__init__(self, *args, **kwargs)
