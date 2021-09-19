import unittest
from pyds import pValue
from numpy.random import normal


class PValueTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=1000)
        b = normal(size=1000)

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
        pass
