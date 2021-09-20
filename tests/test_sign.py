import unittest
from pyds import sign, sort, set, isEqual
from numpy import vectorize, array
from numpy.random import random

round = vectorize(round)


class SignTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(sign(234), 1, msg="Failed to get the sign of a number!")
        self.assertEqual(sign(-234), -1, msg="Failed to get the sign of a number!")
        self.assertEqual(sign(0), 0, msg="Failed to get the sign of a number!")

        a = array([2, -3, 4, -5, 6, 0])
        b = array([1, -1, 1, -1, 1, 0])

        self.assertTrue(
            isEqual(sign(a), b), msg="Failed to get the signs of numbers in an array!"
        )

        a = round(random(size=[10, 10, 10]) * 2 - 1)
        b = sign(a)

        self.assertTrue(
            isEqual(a, b), msg="Failed to get the signs of numbers in an array!"
        )

    def testErrors(self):
        wrongs = [
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
            [2, 3, "four"],
            [[[2, 3, None]]],
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, sign, item)
