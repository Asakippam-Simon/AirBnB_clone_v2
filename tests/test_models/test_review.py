#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime

class test_review(test_basemodel):
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
        cls.review = Review(text="Hear Me Roar!", place_id=cls.place.id,
                            user_id=cls.user.id)
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
        del cls.review
        del cls.filestorage

    def test_attributes(self):
        """Check for attributes."""
        i = Review()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "text"))
        self.assertTrue(hasattr(i, "place_id"))
        self.assertTrue(hasattr(i, "user_id"))

    def test_str(self):
        """ """
        i = self.review.__str__()
        self.assertIn("[Review] ({})".format(self.review.id), i)
        self.assertIn("'id': '{}'".format(self.review.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.review.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.review.updated_at)), i)
        self.assertIn("'text': '{}'".format(self.review.text), i)
        self.assertIn("'user_id': '{}'".format(self.review.user_id), i)
        self.assertIn("'place_id': '{}'".format(self.review.place_id), i)
