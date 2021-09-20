import unittest
from pyds import sort, isEqual
from numpy import array
from numpy.random import *


class SortTestCase(unittest.TestCase):
    def test(self):
        x = [5, 3, 1, 2, 4, 6]
        yTrue = array([1, 2, 3, 4, 5, 6])
        yPred = sort(x)
        self.assertTrue(isEqual(yTrue, yPred), msg="Failed to sort an array!")

        x = normal(size=1000)
        yTrue = array(list(sorted(x.tolist())))
        yPred = sort(x)
        self.assertTrue(isEqual(yTrue, yPred), msg="Failed to sort an array!")

    def testErrors(self):
        wrongs = [
            234,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, sort, item)
