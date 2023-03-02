#!/usr/bin/python3
""" Unittest for 0x0C-python-almost_a_circle Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Tests the Base class's methods and attributes. """

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b21 = Base(21)
        cls.bNeg3 = Base(-3)

    @classmethod
    def tearDownClass(cls):
        Base._Base__nb_objects = 0

    def test_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{}, {}]), "[{}, {}]")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])
        self.assertEqual(Base.from_json_string("[{}, {}]"), [{}, {}])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_create(self):
        with self.assertRaises(TypeError):
            Base.create()

    def test_load_from_file(self):
        self.assertEqual(type(Base.load_from_file()), type([]))


if __name__ == "__main__":
    unittest.main()
