import unittest

import pandas as pd
from numpy.random import random

from pyds import every


class EveryTestCase(unittest.TestCase):
    def test(self):
        x = [2, 3, 4, 5, 6]

        self.assertTrue(every(x, lambda v: v < 7))
        self.assertTrue(every(lambda v: v < 7, x))
        self.assertFalse(every(x, lambda v: v < 6))
        self.assertFalse(every(lambda v: v < 6, x))

        x = [[2, 3, 4], [5, 6]]

        self.assertTrue(every(x, lambda row: type(row) == list))
        self.assertFalse(every(x, lambda row: len(row) > 2))

        x = pd.DataFrame(random(size=[100, 100]))

        self.assertTrue(every(x, lambda row: len(row) == 100))
        self.assertFalse(every(x, lambda row: every(row, lambda v: v > 0.5)))

    def testErrors(self):
        wrongs = [
            [[2, 3, 4], [2, 3, 4]],
            [lambda x: x, lambda x: x],
            [234, 234],
            ["foo", "bar"],
            [True, True],
            [False, False],
            [None, None],
            [{"hello": "world"}, {"hello": "world"}],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, every, pair[0], pair[1])
