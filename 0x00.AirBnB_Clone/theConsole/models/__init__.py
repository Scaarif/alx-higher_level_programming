#!/usr/bin/python3
""" Initialize models package """
from models.engine.file_storage import FileStorage


# create a variable storage, an instance of FileStorage
storage = FileStorage()
# call reload() method on the variable (storage)
storage.reload()  # deserializes the JSON file to __objects
# __objects is a dictionary of objects (instances)
