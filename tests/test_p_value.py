import unittest
from pyds import pValue
from numpy.random import normal


class PValueTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=1000)
        b = a + 0.0001 * normal(size=1000)

        self.assertGreater(
            pValue(a, b),
            0.95,
            msg="Failed to compute the correct p-value for a pair of arrays!",
        )

        b += 1000

        self.assertLess(
            pValue(a, b),
            0.05,
            msg="Failed to compute the correct p-value for a pair of arrays!",
        )

    def testErrors(self):
        missing = normal(size=1000)
        missing[0] = None

        wrongs = [
            [234, 567],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [normal(size=[10, 10]), normal(size=[10, 10])],
            [[1, 2, None], [4, "five", 6]],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, pValue, pair[0], pair[1])
