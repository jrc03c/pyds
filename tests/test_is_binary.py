import unittest

from numpy import *
from numpy.random import *
from pandas import DataFrame, Series

from pyds import isBinary, round


class IsBinaryTestCase(unittest.TestCase):
    def test(self):
        binaries = [
            0,
            1,
            [0, 1],
            round(random(size=100)),
            Series(round(random(size=100))),
            DataFrame(round(random(size=[100, 100]))),
            round(random(size=[100, 100, 100])),
        ]

        for b in binaries:
            self.assertTrue(isBinary(b), msg="Failed to identify binary values!")

        others = [
            234,
            "foo",
            True,
            False,
            None,
            normal(size=100),
            random(size=[100, 100]),
            {"hello": "world"},
            lambda x: x * 2,
            [0, 1, nan],
        ]

        for item in others:
            self.assertFalse(isBinary(item), "Failed to identify non-binary values!")
