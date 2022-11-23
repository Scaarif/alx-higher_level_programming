#!/usr/bin/python3
"""
    Defines the BaseModel class which defines all common attributes
    & or methods for the other classes
"""
import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """ Defines all the common attributes (and methods) for all the
    other classes in the project """
    # Initialize the class
    def __init__(self, *args, **kwargs):
        """ Initializes instances of the class and assigns relevant
        public attributes.
        Note: the instantiation is based on whether **kwargs is provided """
        # args is not used
        # check for **kwargs & if true, re-create an object object_dict
        if kwargs:
            for key, val in kwargs.items():
                # check for time strs and convert to datetime
                if key == 'created_at' or key == 'updated_at':
                    # self.key = val
                    setattr(self, key, datetime.fromisoformat(val))
                # skip __class__ (not an attribute)
                elif key == '__class__':
                    continue  # do nothing
                else:
                    setattr(self, key, val)
        # else, kwargs undefined, initialize normally
        else:
            from models import storage
            # generate a random id (using uuid4) for each instance created
            self.id = str(uuid.uuid4())  # cast the uuid into a string
            # assign current datetime when an object(instance) is created
            self.created_at = datetime.now()
            # track time of update (update it) to current time
            self.updated_at = datetime.now()
            # call storage's new() method - adds an obj to __objects
            storage.new(self)  # add this instance to __objects
            # storage.new(self.to_dict())  # add this instance to __objects

    def __str__(self):
        """ formats the object on print """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at to current
        datetime """
        from models import storage
        self.updated_at = datetime.now()
        # this update isn't reflected in already added obj in __objects
        # let's change that: +include attr added to object after initialization
        # <needed>: access the added object(self) and update its value
        # get this(self) object's key and update its value:
        # this_obj = self.__class__.__name__ + '.' + self.id
        # print('this_object: ', this_obj)
        # this updates both the updated_at attr and adds any new attributes
        # storage.update(this_obj, self.to_dict())
        # call storage's save method: serialize __objects on update
        storage.save()
        # print('updated object: ', self.to_dict())

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
