import unittest

from numpy.random import normal
from pandas import DataFrame, Series

from pyds import distance, magnitude


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
        missing = normal(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            234,
            "foo",
            True,
            False,
            None,
            ["hello", "world"],
            {"hello": "world"},
            lambda x: x * 2,
            missing,
        ]

        for item in wrongs:
            self.assertRaises(
                AssertionError,
                magnitude,
                item,
            )
