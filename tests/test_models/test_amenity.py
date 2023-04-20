#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from datetime import datetime


class test_Amenity(test_basemodel):
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
        cls.user = User(email="lann@houselannister.com", password="revelc")
        cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                          name="Casterly Rock")
        cls.amenity = Amenity(name="gold", place=cls.place.id)
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
        del cls.user
        del cls.place
        del cls.amenity
        del cls.filestorage

    def test_attributes(self):
        """ """
        i = Amenity()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "name"))
        self.assertTrue(hasattr(i, "place_amenities"))

    def test_str(self):
        """ """
        i = self.amenity.__str__()
        self.assertIn("[Amenity] ({})".format(self.amenity.id), i)
        self.assertIn("'id': '{}'".format(self.amenity.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.amenity.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.amenity.updated_at)), i)
        self.assertIn("'name': '{}'".format(self.amenity.name), i)
