#!/usr/bin/python3
""" Defines a class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ define the attributes and methods to serialize and
    deserialize instances using JSON """
    # define (private) class attributes
    __file_path = 'file.json'
    __objects = {}  # a dictionary of objects(<classname>.id: dict?)

    # define public instance methods
    def all(self):
        """ returns the dictionary __objects """
        # recreate the actual instances?
        '''actual_objs = {}
        for key, val in (FileStorage.__objects).items():
            # val is a instance_dict representation
            actual_objs[key] = str(BaseModel(**val))
        return actual_objs'''
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        # assuming obj is an instance dictionary rep
        key = obj.__class__.__name__ + '.' + obj.id
        # key = obj['__class__'] + '.' + obj['id']
        FileStorage.__objects[key] = obj  # append obj to __objects

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path) """
        # dump __objects into file __file_path
        filename = FileStorage.__file_path
        # ===========
        objs_dict = {}
        with open(filename, mode='w', encoding='utf-8') as f:
            for key, obj in (FileStorage.__objects).items():
                objs_dict[key] = obj.to_dict()
            json.dump(objs_dict, f)
            # =================
            # json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists. Else, deos nothing """
        # try to open and read from file
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                # FileStorage.__objects = json.load(f)
                objs_dict = json.load(f)
                for key, obj in objs_dict.items():
                    # recreate the __objects dictionary
                    obj_cls = (key.split('.'))[0]
                    if obj_cls == 'BaseModel':
                        self.new(BaseModel(**obj))
                    elif obj_cls == 'User':
                        self.new(User(**obj))
                    elif obj_cls == 'State':
                        self.new(State(**obj))
                    elif obj_cls == 'City':
                        self.new(City(**obj))
                    elif obj_cls == 'Amenity':
                        self.new(Amenity(**obj))
                    elif obj_cls == 'Place':
                        self.new(Place(**obj))
                    elif obj_cls == 'Review':
                        self.new(Review(**obj))
        except FileNotFoundError:
            pass

    # ===== personal addition (helpers) ==============
    def update(self, obj_key, value):
        """ updates the object with key == obj_key in __objects """
        # assuming obj is an instance dictionary rep
        # check that obj_key exits in __objects
        for key in (FileStorage.__objects).keys():
            if key == obj_key:
                # update obj"s dict_representation (to include all attributes)
                FileStorage.__objects[key] = value  # update objects[key] value
                # print('__objects updated_key: ', FileStorage.__objects[key])
