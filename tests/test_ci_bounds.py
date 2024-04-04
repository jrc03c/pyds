from unittest import TestCase

from numpy.random import normal

from pyds import ciBounds, rScore


class CIBoundsTestCase(TestCase):
    def test(self):
        a = normal(size=100)
        b = a + 0.25 * normal(size=a.shape[0])
        r = rScore(a, b)
        ci = ciBounds(a, b)
        self.assertTrue(ci[0] < r)
        self.assertTrue(ci[1] > r)
        self.assertTrue(r - 0.5 < ci[0])
        self.assertTrue(r + 0.5 > ci[1])
