#!/usr/bin/python3
"""
    Defines the BaseModel class which defines all common attributes
    & or methods for the other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Defines all the common attributes (and methods) for all the
    other classes in the project """
    # Initialize the class
    def __init__(self):
        """ Initializes instances of the class and assigns relevant
        public attributes """
        # generate a random id (using uuid4) for each instance created
        self.id = str(uuid.uuid4())  # cast the uuid into a string
        # assign current datetime when an object(instance) is created
        self.created_at = datetime.now()
        # track time of update (update it) to current time
        self.updated_at = datetime.now()

    def __str__(self):
        """ formats the object on print """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at to current
        datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing:
            1. all keys/values of __dict__ of the instance
            2. a key __class__ with the class name of object
        Note: the datetime objects must be converted to string objects
        in ISO format
        """
        # the dict to return
        class_dict = {}
        # get the __dict__ object and append its values into class_dict
        for key, val in (self.__dict__).items():
            # check for datetime objects and convert them to strings
            if type(val) is datetime:
                class_dict[key] = val.isoformat()
            else:
                class_dict[key] = val
        # add to the dict the __class__ key and its value
        class_dict['__class__'] = self.__class__.__name__
        return class_dict
