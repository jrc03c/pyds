import unittest
from pyds import flatten
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame


class FlattenTestCase(unittest.TestCase):
    def test(self):
        tensors = [
            [2, 3, 4],
            [[2, 3, 4]],
            [[[2, 3, 4]]],
            normal(size=100),
            normal(size=[100, 100]),
            normal(size=[100, 100, 100]),
            Series(normal(size=100)),
            DataFrame(normal(size=[100, 100])),
        ]

        for tensor in tensors:
            self.assertTrue(
                len(shape(flatten(tensor))) == 1, "Failed to flatten tensors!"
            )

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
            pred = flatten(item)
            self.assertEqual(len(pred), 1, msg="Failed to flatten non-tensors!")
            self.assertEqual(pred[0], item, msg="Failed to flatten non-tensors!")
