#!/usr/bin/python3
""" Defines tests for the file_storage module, the FileStorage class """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestFileStorage(unittest.TestCase):
    """ Tests the various attributes &/ methods of FileStorage class """
    def setUp(self):
        """ set up instance objects to use for the tests """
        self.store = FileStorage()
        self.base_test = BaseModel()
        self.classes = ['BaseModel', 'User', 'City', 'State', 'Place',
                        'Amenity', 'Review']

    # test that class instantiates correctly
    def test_instantiation(self):
        """ test that the class correctly instantiates """
        self.assertTrue(isinstance(self.store, FileStorage))

    # test that class attributes are private
    def test_isPrivate__objects_attribute(self):
        """ test that the atribute, objects, is private """
        self.assertEqual(getattr(self.store, 'objects', None), None)

    def test_isPrivate__file_path_attribute(self):
        """ test that the class atribute, file_path is private """
        self.assertEqual(getattr(self.store, '__file_path', None), None)

    # test that the __objects attr is empty at instantiation
    def test_isEmpty__objects_at_instantiation(self):
        """ test that __objects is empty at class instantiation """
        store1 = FileStorage()
        self.assertTrue(len(store1.all()), 0)

    # test that a __file_path is provided?
    def test_isDefined__file_path_at_instantiation(self):
        """ test that __file_path is defined at class instantiation """
        pass

    # test right key assignement for objects(contains class_name& object_id)
    def test_correct_obj_key_assignment_in__objects(self):
        """ test that obj key contains both obj_class_name &
        obj_id """
        objects = self.store.all()
        for obj in objects.keys():
            obj_cls = (obj.split('.'))[0]
            self.assertTrue(obj_cls in self.classes)

    # test all() - return an empty dict on class instantiation
    def test_method_all_return_at_instantiation(self):
        """ test that all() returns an empty dict on
        class instantiation """
        store1 = FileStorage()
        self.assertTrue(len(store1.all()), 0)

    # test all() - return a dict after a BaseModel instantiation
    def test_method_all_return_with__objects(self):
        """ test that all() returns a non empty dict after a save() """
        self.assertTrue(len(self.store.all()) > 0)
        self.assertTrue(len((self.store.all()).keys()) > 0)

    # test new() - correctly sets an obj in __objects on call
    def test_method_new_affects__objects(self):
        """ test that new() sets an obj in (adds obj to) __objects """
        store1 = FileStorage()
        base1 = BaseModel()
        self.assertTrue(f"BaseModel.{base1.id}" in (store1.all()).keys())

    # test save() - writes to a json file(file shouldn't be empty)
    def test_method_save_affects__file_path(self):
        """ test that save() dumps __objects to a file """
        # overwrite contents of file.json ->so its empty(how)?
        store1 = FileStorage()
        base1 = BaseModel()
        # test that file.json is no longer empty(base1 saves)
        store1.reload()
        self.assertTrue(len(store1.all()) > 0)

    # test save() - writes to a json file(file shouldn't be empty)
    def test_method_save_dumps_to__file_path(self):
        """ test that save() dumps __objects to a file """
        self.store.reload()  # affects __objects
        self.assertTrue(len((self.store.all()).keys()) > 0)

    # reload() - that no exception is raised if file isn't found
    def test_method_reload_checks_for__file_path_existence(self):
        """ test that reload() checks for file existence & raises no
        exception if not found """
        # delete the file (file.json)
        self.store.reload()  # then try to reload()
        # assert that no exception is raised (the opposite of assertRaises)
        self.assertTrue(True)
        pass  # to do!
