import unittest
from pyds import getAverageCorrelation
from numpy import *
from numpy.random import *
from pandas import DataFrame


class GetAverageCorrelationTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=[1000, 50])
        b = 0.00001 + a

        self.assertGreater(
            getAverageCorrelation(a, b),
            0.95,
            msg="The average correlation between two almost-identical matrices should be approximately 1!",
        )

        a = random(size=[1000, 50])
        b = random(size=[1000, 50])

        self.assertLess(
            abs(getAverageCorrelation(a, b)),
            0.05,
            msg="The average correlation between two unrelated matrices should be approximately 0!",
        )

        a = DataFrame(a)
        b = DataFrame(b)

        self.assertLess(
            abs(getAverageCorrelation(a, b)),
            0.05,
            msg="The average correlation between two unrelated matrices should be approximately 0!",
        )

    def testErrors(self):
        wrongs = [
            [[2, 3, 4], [5, 6, 7]],
            [normal(size=[3, 3, 3]), normal(size=[3, 3, 3])],
            [234, 567],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [[["a", "b", "c"]], [["1", "2", "3"]]],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, getAverageCorrelation, pair[0], pair[1])
