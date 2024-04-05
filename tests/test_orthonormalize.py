import unittest

from numpy import dot, eye
from numpy.random import normal, random
from pandas import DataFrame

from pyds import orthonormalize, rScore


class OrthonormalizeTestCase(unittest.TestCase):
    def test(self):
        x = orthonormalize(random(size=[10000, 10]))
        r = rScore(eye(10), dot(x.T, x))
        self.assertGreater(r, 0.95)

        x = DataFrame(x)
        r = rScore(eye(10), dot(x.T, x))
        self.assertGreater(r, 0.95)

    def testErrors(self):
        wrongs = [
            normal(size=1000),
            normal(size=[10, 10, 10]),
            234,
            "foo",
            True,
            False,
            None,
            {},
            lambda x: x,
            [[2, "3"], [4, 5]],
        ]

        for item in wrongs:
            self.assertRaises(Exception, orthonormalize, item)
