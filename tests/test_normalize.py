import unittest

from numpy import mean, std
from numpy.random import normal
from pandas import DataFrame as DF

from pyds import chop, normalize


class NormalizeTestCase(unittest.TestCase):
    def test(self):
        x = normal(size=[10, 10, 10, 10])
        y = normalize(x)

        self.assertEqual(chop(mean(y)), 0)
        self.assertEqual(chop(std(y) - 1), 0)

        x = DF(normal(size=[100, 100]))
        y = normalize(x)

        self.assertEqual(chop(mean(y)), 0)
        self.assertEqual(chop(std(y) - 1), 0)

    def testErrors(self):
        wrongs = [[2, "3", 4], 234, "foo", True, False, None, lambda x: x, {}]

        for item in wrongs:
            self.assertRaises(Exception, normalize, item)
