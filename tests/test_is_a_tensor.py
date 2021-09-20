import unittest
from pyds import isATensor
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame


class IsATensorTestCase(unittest.TestCase):
    def test(self):
        tensors = [
            [2, 3, 4],
            [[2, 3, 4]],
            [[[2, 3, 4]]],
            normal(size=100),
            normal(size=[100, 100]),
            normal(size=[100, 100, 100]),
            DataFrame(normal(size=[100, 100])),
            Series(normal(size=100)),
        ]

        for tensor in tensors:
            self.assertTrue(isATensor(tensor), msg="Failed to identify tensors!")

        others = [
            234,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in others:
            self.assertFalse(isATensor(item), msg="Failed to identify non-tensors!")
