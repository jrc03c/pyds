import unittest
from pyds import sort, isEqual
from numpy.random import *


class SortTestCase(unittest.TestCase):
    def test(self):
        x = [5, 3, 1, 2, 4, 6]
        yTrue = [1, 2, 3, 4, 5, 6]
        yPred = sort(x)
        self.assertTrue(isEqual(yTrue, yPred), msg="Failed to sort an array!")

        x = normal(size=1000)
        yTrue = list(sorted(x.tolist()))
        yPred = sort(x)
        self.assertTrue(isEqual(yTrue, yPred), msg="Failed to sort an array!")

    def testErrors(self):
        self.assertTrue(False)
