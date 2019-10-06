#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertRaises(TypeError, max_integer, [])

    def test_neg(self):
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)

    def test_floats(self):
        self.assertAlmostEqual(max_integer([1.2, 2.3, 3.4]), 3.4)

    def test_tuple_str(self):
        self.assertAlmostEqual(max_integer(("Hola", "Mundo", "valen")), "valen")

    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)

    def test_tuple_int(self):
        self.assertAlmostEqual(max_integer((1, 2, 8)), 8)

    def test_str_param(self):
        self.assertAlmostEqual(max_integer("Yehaa"), "h")

    def test_tuple_str(self):
        self.assertRaises(TypeError, max_integer, (1, "Holi", 58))

    def test_list_str(self):
        self.assertRaises(TypeError, max_integer, [1, "Holi", 3])

    def test_empty(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_boolean(self):
        self.assertRaises(TypeError, max_integer, True)

    def test_list_dict(self):
        self.assertRaises(TypeError, max_integer, [{"hola": 4, "mundo": 5}, 2])
