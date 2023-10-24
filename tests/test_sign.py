import unittest

from numpy import array
from numpy.random import random

from pyds import isEqual, round, sign


class SignTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(sign(234), 1, msg="Failed to get the sign of a number!")

        self.assertEqual(
            type(sign(234)),
            int,
            msg="Failed to return a single value for the sign of a single number!",
        )

        self.assertEqual(sign(-234), -1, msg="Failed to get the sign of a number!")

        self.assertEqual(
            type(sign(-234)),
            int,
            msg="Failed to return a single value for the sign of a single number!",
        )

        self.assertEqual(sign(0), 0, msg="Failed to get the sign of a number!")

        self.assertEqual(
            type(sign(0)),
            int,
            msg="Failed to return a single value for the sign of a single number!",
        )

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
        missing = random(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
            [2, 3, "four"],
            [[[2, 3, None]]],
            missing,
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, sign, item)
