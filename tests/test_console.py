#!/usr/bin/python3
"""
Contains the unittests for console.py
"""

from io import StringIO
import console
import inspect
import pycodestyle
import sys
import unittest
from unittest.mock import patch
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to Pycodestyle"""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestConsoleFunc(unittest.TestCase):
    """
    Testing the functionality of console.py
    """
    def test_help(self):
        """
        Testing the help method
        """
        out = "Prints an instance based on the class name and id\n"
        out2 = "Handling the EOF command\n"
        out3 = "Quit command to exit the program\n"
        out4 = "*** No help on emptyline\n"
        out5 = "Creates a new instance and prints the id\n"
        out6 = "Deletes an instance based on the class name and id\n"
        out7 = "Prints all string representation of all instances\n"
        out8 = "Updates an instance based on the class name and id\n"
        out9 = "*** No help on default\n"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), out2)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), out3)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help emptyline")
            self.assertEqual(f.getvalue(), out4)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), out5)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue(), out6)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue(), out7)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue(), out8)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help default")
            self.assertEqual(f.getvalue(), out9)
