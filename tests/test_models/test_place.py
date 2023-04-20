#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class test_Place(test_basemodel):
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
        del cls.filestorage

    def test_attributes(self):
        """Check for attributes."""
        i = Place()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "city_id"))
        self.assertTrue(hasattr(i, "name"))
        self.assertTrue(hasattr(i, "description"))
        self.assertTrue(hasattr(i, "number_rooms"))
        self.assertTrue(hasattr(i, "number_bathrooms"))
        self.assertTrue(hasattr(i, "max_guest"))
        self.assertTrue(hasattr(i, "price_by_night"))
        self.assertTrue(hasattr(i, "latitude"))
        self.assertTrue(hasattr(i, "longitude"))

    def test_str(self):
        """ """
        i = self.place.__str__()
        self.assertIn("[Place] ({})".format(self.place.id), i)
        self.assertIn("'id': '{}'".format(self.place.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.place.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.place.updated_at)), i)
        self.assertIn("'city_id': '{}'".format(self.place.city_id), i)
        self.assertIn("'user_id': '{}'".format(self.place.user_id), i)
        self.assertIn("'name': '{}'".format(self.place.name), i)
