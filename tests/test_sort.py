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

        x = [{"name": "Alice"}, {"name": "Charlie"}, {"name": "Bob"}]
        yTrue = array([{"name": "Charlie"}, {"name": "Bob"}, {"name": "Alice"}])
        yPred1 = sort(x, lambda a, b: 1 if a["name"] < b["name"] else -1)
        yPred2 = sort(lambda a, b: 1 if a["name"] < b["name"] else -1, x)

        self.assertTrue(
            isEqual(yTrue, yPred1), msg="Failed to sort an array of objects!"
        )

        self.assertTrue(
            isEqual(yTrue, yPred2), msg="Failed to sort an array of objects!"
        )

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
