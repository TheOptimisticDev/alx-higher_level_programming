#!/usr/bin/python3
""" Unittest for 0x0C-python-almost_a_circle Rectangle class
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class's methods and attributes. """

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)
        cls.r2 = Rectangle(2, 2, 0, 0)
        cls.r200 = Rectangle(20, 10, id=200)
        cls.r201 = Rectangle(20, 10, 1, 1)

    @classmethod
    def tearDownClass(cls):
        Rectangle._Base__nb_objects = 0
        Base._Base__nb_objects = 0

    def test_init(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(21)
        with self.assertRaises(TypeError):
            Rectangle(-3)
        with self.assertRaises(TypeError):
            Rectangle(0)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r200.id, 200)
        self.assertEqual(self.r201.id, 3)

    def test__str__(self):
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 1/1")
        self.assertEqual(str(self.r200), "[Rectangle] (200) 0/0 - 20/10")
        self.assertEqual(str(self.r201), "[Rectangle] (3) 1/1 - 20/10")

    def test_properties(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r201.width, 20)
        self.assertEqual(self.r201.height, 10)
        self.assertEqual(self.r201.x, 1)
        self.assertEqual(self.r201.y, 1)

    def test_width_setter(self):
        with self.assertRaises(TypeError):
            self.r2.width = '1'
        with self.assertRaises(TypeError):
            self.r2.width = [1, 2]
        with self.assertRaises(TypeError):
            self.r2.width = {1, 2}
        with self.assertRaises(TypeError):
            self.r2.width = {1: 2}
        with self.assertRaises(TypeError):
            self.r2.width = 1, 2
        with self.assertRaises(TypeError):
            self.r2.width = True
        with self.assertRaises(ValueError):
            self.r2.width = -5
        with self.assertRaises(ValueError):
            self.r2.width = 0
        self.r2.width = 5
        self.assertEqual(self.r2.width, 5)

    def test_height_setter(self):
        with self.assertRaises(TypeError):
            self.r2.height = '1'
        with self.assertRaises(TypeError):
            self.r2.height = [1, 2]
        with self.assertRaises(TypeError):
            self.r2.height = {1, 2}
        with self.assertRaises(TypeError):
            self.r2.height = {1: 2}
        with self.assertRaises(TypeError):
            self.r2.height = 1, 2
        with self.assertRaises(TypeError):
            self.r2.height = True
        with self.assertRaises(ValueError):
            self.r2.height = -5
        with self.assertRaises(ValueError):
            self.r2.height = 0
        self.r2.height = 5
        self.assertEqual(self.r2.height, 5)

    def test_x_setter(self):
        with self.assertRaises(TypeError):
            self.r2.x = '1'
        with self.assertRaises(TypeError):
            self.r2.x = [1, 2]
        with self.assertRaises(TypeError):
            self.r2.x = {1, 2}
        with self.assertRaises(TypeError):
            self.r2.x = {1: 2}
        with self.assertRaises(TypeError):
            self.r2.x = 1, 2
        with self.assertRaises(TypeError):
            self.r2.x = True
        with self.assertRaises(ValueError):
            self.r2.x = -5
        self.r2.x = 5
        self.assertEqual(self.r2.x, 5)
        self.r2.x = 0
        self.assertEqual(self.r2.x, 0)

    def test_y_setter(self):
        with self.assertRaises(TypeError):
            self.r2.y = '1'
        with self.assertRaises(TypeError):
            self.r2.y = [1, 2]
        with self.assertRaises(TypeError):
            self.r2.y = {1, 2}
        with self.assertRaises(TypeError):
            self.r2.y = {1: 2}
        with self.assertRaises(TypeError):
            self.r2.y = 1, 2
        with self.assertRaises(TypeError):
            self.r2.y = True
        with self.assertRaises(ValueError):
            self.r2.y = -5
        self.r2.y = 5
        self.assertEqual(self.r2.y, 5)
        self.r2.y = 0
        self.assertEqual(self.r2.y, 0)

    def test_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r200.area(), 200)

    def test_display(self):
        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        self.r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput1.getvalue(), "#\n")
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        self.r2.update(2, 2, 2, 2, 2)
        self.r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput2.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_args(self):
        self.r2.update(2)
        self.assertEqual(self.r2.id, 2)
        self.r2.update(22)
        self.assertEqual(self.r2.id, 22)
        self.r2.update(2, 2, 2, 2, 2)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 2/2 - 2/2")
        self.r2.update(2, 3)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 2/2 - 3/2")
        self.r2.update(2, 3, 4)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 2/2 - 3/4")
        self.r2.update(2, 3, 4, 5)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 5/2 - 3/4")
        self.r2.update(2, 3, 4, 5, 6, 7)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 5/6 - 3/4")

    def test_update_kwargs(self):
        self.r2.update(id=7)
        self.assertEqual(self.r2.id, 7)
        self.r2.update(width=8, id=8)
        self.assertEqual(self.r2.id, 8)
        self.assertEqual(self.r2.width, 8)
        self.r2.update(height=9, width=9, id=9)
        self.assertEqual(self.r2.id, 9)
        self.assertEqual(self.r2.width, 9)
        self.assertEqual(self.r2.height, 9)
        self.r2.update(x=10, height=10, width=10, id=10)
        self.assertEqual(self.r2.id, 10)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 10)
        self.r2.update(x=2, height=2, y=2, width=2, id=2)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 2/2 - 2/2")

    def test_to_dictionary(self):
        self.assertEqual(self.r1.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        self.assertEqual(self.r201.to_dictionary(),
                         {'id': 3, 'width': 20, 'height': 10, 'x': 1, 'y': 1})

    def test_to_json_string(self):
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string([{}]), "[{}]")
        self.assertEqual(Rectangle.to_json_string([{}, {}]), "[{}, {}]")

    def test_from_json_string(self):
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])
        self.assertEqual(Rectangle.from_json_string("[{}]"), [{}])
        self.assertEqual(Rectangle.from_json_string("[{}, {}]"), [{}, {}])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_create(self):
        nb_prior = Rectangle._Base__nb_objects
        r90 = Rectangle.create(id=90)
        self.assertEqual(str(r90), "[Rectangle] (90) 0/0 - 1/1")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r91 = Rectangle.create(id=91, y=1)
        self.assertEqual(str(r91), "[Rectangle] (91) 0/1 - 1/1")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r92 = Rectangle.create(id=92, x=1)
        self.assertEqual(str(r92), "[Rectangle] (92) 1/0 - 1/1")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r93 = Rectangle.create(id=93, width=3)
        self.assertEqual(str(r93), "[Rectangle] (93) 0/0 - 3/1")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r94 = Rectangle.create(id=94, height=4)
        self.assertEqual(str(r94), "[Rectangle] (94) 0/0 - 1/4")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r95 = Rectangle.create(id=95, x=5, y=5)
        self.assertEqual(str(r95), "[Rectangle] (95) 5/5 - 1/1")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r96 = Rectangle.create(id=96, width=5, height=6)
        self.assertEqual(str(r96), "[Rectangle] (96) 0/0 - 5/6")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r97 = Rectangle.create(id=97, height=7, width=6, y=5, x=4)
        self.assertEqual(str(r97), "[Rectangle] (97) 4/5 - 6/7")
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r98 = Rectangle.create(x=98, y=99)
        self.assertEqual(str(r98),
                         "[Rectangle] ({:d}) 98/99 - 1/1".format(nb_prior + 1))
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r99 = Rectangle.create(height=99, width=98)
        self.assertEqual(str(r99),
                         "[Rectangle] ({:d}) 0/0 - 98/99".format(nb_prior + 1))
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)
        nb_prior = Rectangle._Base__nb_objects
        r100 = Rectangle.create()
        self.assertEqual(str(r100),
                         "[Rectangle] ({:d}) 0/0 - 1/1".format(nb_prior + 1))
        self.assertEqual(Rectangle._Base__nb_objects, nb_prior + 1)

    def test_load_from_file(self):
        self.assertEqual(type(Rectangle.load_from_file()), type([]))


if __name__ == "__main__":
    unittest.main()
