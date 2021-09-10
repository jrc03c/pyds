import unittest
from pyds import getAverageCorrelation
from numpy import *
from numpy.random import *


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

    def testErrors(self):
        self.assertRaises(AssertionError, getAverageCorrelation, [1, 2, 3], [4, 5, 6])

        self.assertRaises(
            AssertionError,
            getAverageCorrelation,
            normal(size=[3, 3, 3]),
            normal(size=[3, 3, 3]),
        )

        self.assertRaises(AssertionError, getAverageCorrelation, "foo", "bar")

        self.assertRaises(AssertionError, getAverageCorrelation, True, False)

        self.assertRaises(
            AssertionError, getAverageCorrelation, lambda x: x * 2, lambda x: x * 3
        )

        self.assertRaises(
            AssertionError,
            getAverageCorrelation,
            [["a", "b", "c"]],
            [["one", "two", "three"]],
        )
