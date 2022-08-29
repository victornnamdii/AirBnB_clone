#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
from datetime import datetime
import inspect
from models import base_model
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = base_model.BaseModel
module_doc = base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """
    Tests the functionality of the BaseModel
    """
    def TestInit(self):
        """
        Tests the initialization of the class
        """
        hold = BaseModel()
        self.assertIs(type(hold), BaseModel)
        hold.name = "duba"
        hold.number = 77
        attr = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
                "number": int
        }
        for att, typ in attr.items():
            with self.subTest(att=att, typ=typ):
                self.assertIn(attr, hold.__dict__)
                self.assertIs(type(hold.__dict__[att]), typ)
        self.assertEqual(hold.name, "duba")
        self.assertEqual(hold.number, 77)


if __name__ == '__main__':
    unittest.main()
