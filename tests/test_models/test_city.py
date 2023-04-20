#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime


class test_City(test_basemodel):
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
        cls.city = City(name="Lannisport", state_id=cls.state.id)
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
        del cls.city
        del cls.filestorage

    def test_attributes(self):
        """ """
        i = City()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "name"))
        self.assertTrue(hasattr(i, "state_id"))

    def test_str(self):
        """ """
        i = self.city.__str__()
        self.assertIn("[City] ({})".format(self.city.id), i)
        self.assertIn("'id': '{}'".format(self.city.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.city.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.city.updated_at)), i)
        self.assertIn("'name': '{}'".format(self.city.name), i)
