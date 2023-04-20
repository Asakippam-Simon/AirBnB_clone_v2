#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime

class test_state(test_basemodel):
    """ """

    @classmethod
    def setUpClass(cls):
        """ """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.state = State(name="Western coast")
        cls.filestorage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """ """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.state
        del cls.filestorage

    def test_attributes(self):
        """ """
        i = State()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "name"))

    def test_str(self):
        """ """
        i = self.state.__str__()
        self.assertIn("[State] ({})".format(self.state.id), i)
        self.assertIn("'id': '{}'".format(self.state.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.state.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.state.updated_at)), i)
        self.assertIn("'name': '{}'".format(self.state.name), i)
