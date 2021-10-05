# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Margaret Lehmann
"""

import unittest

from triangle_method import classify_triangle

# This code implements the unit test functionality


class TestTriangles(unittest.TestCase):
    """Class to test the triangle method"""

    def test_right_triangle_a(self):
        """Tests correct right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_b(self):
        """Tests correct right triangle in a different order"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right')

    def test_equilateral_triangles(self):
        """Tests correct equilateral triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_scalene_triangles(self):
        """Tests correct scalene triangle"""
        self.assertEqual(classify_triangle(6, 7, 9), 'Scalene')

    def test_isosceles_triangles(self):
        """Tests correct isosceles triangle"""
        self.assertEqual(classify_triangle(7, 7, 9), 'Isosceles')

    def test_not_a_triangle(self):
        """Tests invalid triangle sides"""
        self.assertEqual(classify_triangle(3, 3, 9), 'NotATriangle')

    def test_invalid_input_a(self):
        """Tests negative triangle sides"""
        self.assertEqual(classify_triangle(3, 3, -3), 'InvalidInput')

    def test_invalid_input_b(self):
        """Tests too big triangle sides"""
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput')

    def test_invalid_input_c(self):
        """Tests not a number triangle sides"""
        self.assertEqual(classify_triangle(3, "hello", 11), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
