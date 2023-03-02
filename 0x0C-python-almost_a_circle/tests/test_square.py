#!/usr/bin/python3
""" Unittest for 0x0C-python-almost_a_circle Square class
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests the Square class's methods and attributes. """

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(1)
        cls.s2 = Square(2, 0, 0)
        cls.s200 = Square(20, id=200)
        cls.s201 = Square(20, 1, 1)

    @classmethod
    def tearDownClass(cls):
        Square._Base__nb_objects = 0

    def test_init(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(ValueError):
            Square(-3)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1, 1)
        with self.assertRaises(ValueError):
            Square(1, -1, 1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_id(self):
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s200.id, 200)
        self.assertEqual(self.s201.id, 3)

    def test__str__(self):
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s200), "[Square] (200) 0/0 - 20")
        self.assertEqual(str(self.s201), "[Square] (3) 1/1 - 20")

    def test_properties(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s201.size, 20)
        self.assertEqual(self.s201.x, 1)
        self.assertEqual(self.s201.y, 1)

    def test_size_setter(self):
        with self.assertRaises(TypeError):
            self.s2.size = '1'
        with self.assertRaises(TypeError):
            self.s2.size = [1, 2]
        with self.assertRaises(TypeError):
            self.s2.size = {1, 2}
        with self.assertRaises(TypeError):
            self.s2.size = {1: 2}
        with self.assertRaises(TypeError):
            self.s2.size = 1, 2
        with self.assertRaises(TypeError):
            self.s2.size = True
        with self.assertRaises(ValueError):
            self.s2.size = -5
        with self.assertRaises(ValueError):
            self.s2.size = 0
        self.s2.size = 5
        self.assertEqual(self.s2.size, 5)

    def test_x_setter(self):
        with self.assertRaises(TypeError):
            self.s2.x = '1'
        with self.assertRaises(TypeError):
            self.s2.x = [1, 2]
        with self.assertRaises(TypeError):
            self.s2.x = {1, 2}
        with self.assertRaises(TypeError):
            self.s2.x = {1: 2}
        with self.assertRaises(TypeError):
            self.s2.x = 1, 2
        with self.assertRaises(TypeError):
            self.s2.x = True
        with self.assertRaises(ValueError):
            self.s2.x = -5
        self.s2.x = 5
        self.assertEqual(self.s2.x, 5)
        self.s2.x = 0
        self.assertEqual(self.s2.x, 0)

    def test_y_setter(self):
        with self.assertRaises(TypeError):
            self.s2.y = '1'
        with self.assertRaises(TypeError):
            self.s2.y = [1, 2]
        with self.assertRaises(TypeError):
            self.s2.y = {1, 2}
        with self.assertRaises(TypeError):
            self.s2.y = {1: 2}
        with self.assertRaises(TypeError):
            self.s2.y = 1, 2
        with self.assertRaises(TypeError):
            self.s2.y = True
        with self.assertRaises(ValueError):
            self.s2.y = -5
        self.s2.y = 5
        self.assertEqual(self.s2.y, 5)
        self.s2.y = 0
        self.assertEqual(self.s2.y, 0)

    def test_area(self):
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s200.area(), 400)

    def test_display(self):
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        self.s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput1.getvalue(), "#\n")
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        self.s2.update(2, 2, 2, 2)
        self.s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput2.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_args(self):
        self.s2.update(2)
        self.assertEqual(self.s2.id, 2)
        self.s2.update(22)
        self.assertEqual(self.s2.id, 22)
        self.s2.update(2, 2, 2, 2)
        self.assertEqual(str(self.s2), "[Square] (2) 2/2 - 2")
        self.s2.update(2, 3)
        self.assertEqual(str(self.s2), "[Square] (2) 2/2 - 3")
        self.s2.update(2, 3, 4)
        self.assertEqual(str(self.s2), "[Square] (2) 4/2 - 3")
        self.s2.update(2, 3, 4, 5)
        self.assertEqual(str(self.s2), "[Square] (2) 4/5 - 3")
        self.s2.update(2, 3, 4, 5, 6, 7)
        self.assertEqual(str(self.s2), "[Square] (2) 4/5 - 3")

    def test_update_kwargs(self):
        self.s2.update(id=7)
        self.assertEqual(self.s2.id, 7)
        self.s2.update(size=8, id=8)
        self.assertEqual(self.s2.id, 8)
        self.assertEqual(self.s2.size, 8)
        self.s2.update(x=9, size=9, id=9)
        self.assertEqual(self.s2.id, 9)
        self.assertEqual(self.s2.size, 9)
        self.assertEqual(self.s2.x, 9)
        self.s2.update(x=2, y=2, size=2, id=2)
        self.assertEqual(str(self.s2), "[Square] (2) 2/2 - 2")

    def test_to_dictionary(self):
        self.assertEqual(self.s1.to_dictionary(),
                         {'id': 1, 'size': 1, 'x': 0, 'y': 0})
        self.assertEqual(self.s201.to_dictionary(),
                         {'id': 3, 'size': 20, 'x': 1, 'y': 1})

    def test_to_json_string(self):
        self.assertEqual(Square.to_json_string(None), "[]")
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string([{}]), "[{}]")
        self.assertEqual(Square.to_json_string([{}, {}]), "[{}, {}]")

    def test_from_json_string(self):
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Square.from_json_string(""), [])
        self.assertEqual(Square.from_json_string("[]"), [])
        self.assertEqual(Square.from_json_string("[{}]"), [{}])
        self.assertEqual(Square.from_json_string("[{}, {}]"), [{}, {}])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_create(self):
        nb_prior = Base._Base__nb_objects
        s90 = Square.create(id=90)
        self.assertEqual(str(s90), "[Square] (90) 0/0 - 1")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s91 = Square.create(id=91, y=1)
        self.assertEqual(str(s91), "[Square] (91) 0/1 - 1")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s92 = Square.create(id=92, x=1)
        self.assertEqual(str(s92), "[Square] (92) 1/0 - 1")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s93 = Square.create(id=93, size=3)
        self.assertEqual(str(s93), "[Square] (93) 0/0 - 3")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s94 = Square.create(id=94, x=3, size=4)
        self.assertEqual(str(s94), "[Square] (94) 3/0 - 4")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s95 = Square.create(id=95, x=5, y=5)
        self.assertEqual(str(s95), "[Square] (95) 5/5 - 1")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s96 = Square.create(id=96, size=5, y=6)
        self.assertEqual(str(s96), "[Square] (96) 0/6 - 5")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s97 = Square.create(id=97, size=7, y=6, x=5)
        self.assertEqual(str(s97), "[Square] (97) 5/6 - 7")
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s98 = Square.create(x=98, y=97)
        self.assertEqual(str(s98),
                         "[Square] ({:d}) 98/97 - 1".format(nb_prior + 1))
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s99 = Square.create(size=99)
        self.assertEqual(str(s99),
                         "[Square] ({:d}) 0/0 - 99".format(nb_prior + 1))
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)
        nb_prior = Base._Base__nb_objects
        s100 = Square.create()
        self.assertEqual(str(s100),
                         "[Square] ({:d}) 0/0 - 1".format(nb_prior + 1))
        self.assertEqual(Base._Base__nb_objects, nb_prior + 1)

    def test_load_from_file(self):
        self.assertEqual(type(Square.load_from_file()), type([]))


if __name__ == "__main__":
    unittest.main()
