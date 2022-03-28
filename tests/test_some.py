from numpy.random import random
from pyds import flatten, some
import pandas as pd
import unittest


class SomeTestCase(unittest.TestCase):
    def test(self):
        x = [2, 3, 4, 5, 6]

        self.assertTrue(some(x, lambda v: v < 5))
        self.assertTrue(some(lambda v: v < 5, x))
        self.assertFalse(some(x, lambda v: v < 2))
        self.assertFalse(some(lambda v: v < 2, x))

        x = [[2, 3, 4], [5, 6], "foo", 234, True, False, None, {}, lambda x: x]

        self.assertTrue(some(x, lambda item: type(item) == list))
        self.assertFalse(some(x, lambda item: item == "hello"))

        x = pd.DataFrame(random(size=[100, 100]))

        self.assertTrue(some(x, lambda row: some(row, lambda v: v > 0.5)))
        self.assertFalse(some(x, lambda row: len(row) < 100))

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
            self.assertRaises(AssertionError, some, pair[0], pair[1])
