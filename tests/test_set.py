import unittest
from pyds import sort, set, isEqual, range
from pandas import Series, DataFrame
from numpy import array
from numpy.random import normal


class SetTestCase(unittest.TestCase):
    def test(self):
        x = [2, 3, 2, 3, 3, 3, 4, 5, 6, 3]
        yTrue = array([2, 3, 4, 5, 6])
        yPred = sort(set(x))

        self.assertTrue(
            isEqual(yTrue, yPred), msg="Failed to get the set of values from a tensor!"
        )

        a = range(0, 100)
        b = set(a)

        self.assertTrue(
            isEqual(a, b), msg="Failed to get the set of values from a tensor!"
        )

        x = [[2, 3], [3, 4, 5], [[2], [3, 4, 5]]]
        yTrue = array([2, 3, 4, 5])
        yPred = sort(set(x))

        self.assertTrue(
            isEqual(yTrue, yPred), msg="Failed to get the set of values from a tensor!"
        )

        try:
            set(DataFrame(normal(size=[100, 100])))
            failed = False
        except:
            failed = True

        self.assertFalse(failed, msg="Failed to get the set of values from a tensor!")

        try:
            set(Series(normal(size=1000)))
            failed = False
        except:
            failed = True

        self.assertFalse(failed, msg="Failed to get the set of values from a tensor!")

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
            self.assertRaises(AssertionError, set, item)
