import unittest
from pyds import isIterable
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame


class IsIterableTestCase(unittest.TestCase):
    def test(self):
        iterables = [
            [2, 3, 4],
            [[2, 3, 4]],
            [[[2, 3, 4]]],
            normal(size=100),
            normal(size=[100, 100]),
            normal(size=[100, 100, 100]),
            Series(normal(size=100)),
            DataFrame(normal(size=[100, 100])),
            "foo",
            {"hello": "world"},
        ]

        for i in iterables:
            self.assertTrue(isIterable(i), msg="Failed to identify iterables!")

        others = [
            234,
            True,
            False,
            None,
            lambda x: x * 2,
        ]

        for item in others:
            self.assertFalse(isIterable(item), msg="Failed to identify non-iterables!")
