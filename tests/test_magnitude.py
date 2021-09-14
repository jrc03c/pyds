import unittest
from pyds import magnitude, distance
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame


class MagnitudeTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            magnitude([3, 4]), 5, msg="Failed to computed magnitude of tensors!"
        )

        tensors = [
            normal(size=100),
            normal(size=[100, 100]),
            normal(size=[100, 100, 100]),
            Series(normal(size=100)),
            DataFrame(normal(size=[100, 100])),
        ]

        for tensor in tensors:
            self.assertAlmostEqual(
                magnitude(tensor),
                distance(tensor, 0),
                msg="Failed to computed magnitude of tensors!",
            )

    def testErrors(self):
        wrongs = [
            234,
            "foo",
            True,
            False,
            None,
            ["hello", "world"],
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in wrongs:
            self.assertRaises(
                AssertionError, magnitude, item,
            )
