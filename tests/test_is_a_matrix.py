import unittest

from numpy.random import normal
from pandas import DataFrame, Series

from pyds import isAMatrix


class IsAMatrixTestCase(unittest.TestCase):
    def test(self):
        matrices = [
            [[2, 3, 4], [5, 6, 7]],
            normal(size=[100, 100]),
            DataFrame(normal(size=[100, 100])),
        ]

        for matrix in matrices:
            self.assertTrue(isAMatrix(matrix), msg="Failed to identify matrices!")

        others = [
            [2, 3, 4],
            [[[2, 3, 4]]],
            normal(size=100),
            normal(size=[100, 100, 100]),
            Series(normal(size=100)),
            234,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in others:
            self.assertFalse(isAMatrix(item), msg="Failed to identify non-matrices!")
