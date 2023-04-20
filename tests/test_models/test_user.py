#!/usr/bin/python3
""" """
import os
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime

class test_User(test_basemodel):
    """ """

    @classmethod
    def setUpClass(cls):
        """ """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.user = User(email="lann@houselannister.com", password="revelc")
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
        del cls.user
        del cls.filestorage

    def test_attributes(self):
        """ """
        i = User()
        self.assertEqual(str, type(i.id))
        self.assertEqual(datetime, type(i.created_at))
        self.assertEqual(datetime, type(i.updated_at))
        self.assertTrue(hasattr(i, "__tablename__"))
        self.assertTrue(hasattr(i, "email"))
        self.assertTrue(hasattr(i, "password"))
        self.assertTrue(hasattr(i, "first_name"))
        self.assertTrue(hasattr(i, "last_name"))

    def test_str(self):
        """ """
        i = self.user.__str__()
        self.assertIn("[User] ({})".format(self.user.id), i)
        self.assertIn("'id': '{}'".format(self.user.id), i)
        self.assertIn("'created_at': {}".format(
            repr(self.user.created_at)), i)
        self.assertIn("'updated_at': {}".format(
            repr(self.user.updated_at)), i)
        self.assertIn("'email': '{}'".format(self.user.email), i)
        self.assertIn("'password': '{}'".format(self.user.password), i)
