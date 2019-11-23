#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up test cases"""
        cls.base = BaseModel()

    @classmethod
    def teardown(cls):
        """Cleans memory after tests"""
        del cls.base
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        """PEP8 style test"""
        guide = pep8.StyleGuide(quit=True)
        rev = guide.check_files(["models/base_model.py"])
        self.assertEqual(rev.total_errors, 0, "Fix Style")

    def test_docstring(self):
        """Checks for docs"""
        for doc_fun in dir(BaseModel):
            self.assertIsNotNone(doc_fun.__doc__)

    def test_init(self):
        """Tests for the __init__"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_check_public_attributes(self):
        """Check if the public attributes of the instance exist"""
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

    def test_check_methods(self):
        """Check if the methods exist"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_id_assignment(self):
        """Check if id is being assigned"""
        self.assertEqual(str, type(self.base.id))

    def test_created_at_assignment(self):
        """Check if created_at is being assigned"""
        self.assertEqual(datetime, type(self.base.created_at))

    def test_updated_at_assignment(self):
        """Check if updated_at is being assigned"""
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_save(self):
        """Tests save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """Tests to_dict method"""
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue("to_dict" in dir(self.base))

if __name__ == "__main__":
    unittest.main()
