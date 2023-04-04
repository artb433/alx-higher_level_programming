#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.fun = max_integer

    def testListLen(self):
        self.assertEqual(max_integer([]), None)

    def testNegativeValues(self):
        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    def testString(self):
        arg = ["string", "another", "yet another"]

        self.assertEqual(self.fun(arg), "yet another")

    def testMatrix(self):
        ret_val = max_integer([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(ret_val, [5, 6])

    def testDict(self):
        arg = [{'one': 1, 'two': 2}, {'three': 3, 'four': 4}]

        self.assertRaises(TypeError, self.fun, arg)

    def testTupleParam(self):
        arg = ([1, 2, 3], [4, 5, 6])

        self.assertEqual(self.fun(arg), [4, 5, 6])

    def testMultipleTypes(self):
        arg = ["hello", 5, [5, 10], [{'one': 1}, {'two': 2}]]

        self.assertRaises(TypeError, self.fun, arg)
