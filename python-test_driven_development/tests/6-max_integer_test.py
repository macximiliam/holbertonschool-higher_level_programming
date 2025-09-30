#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -1, -20]), -1)

    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.6, 0.9]), 2.6)

    def test_mix_int_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_string_list(self):
        self.assertEqual(max_integer("holberton"), 't')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == '__main__':
    unittest.main()
