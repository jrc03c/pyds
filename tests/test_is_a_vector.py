import unittest
from pyds import isAVector
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame


class IsAVectorTestCase(unittest.TestCase):
    def test(self):
        vectors = [
            [2, 3, 4],
            normal(size=100),
            Series(normal(size=100)),
        ]

        for vector in vectors:
            self.assertTrue(isAVector(vector), msg="Failed to identify vectors!")

        others = [
            [[2, 3, 4]],
            [[[2, 3, 4]]],
            normal(size=[100, 100]),
            normal(size=[100, 100, 100]),
            DataFrame(normal(size=[100, 100])),
            234,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in others:
            self.assertFalse(isAVector(item), msg="Failed to identify non-vectors!")
