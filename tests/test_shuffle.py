import unittest

from numpy import shape
from numpy.random import normal
from pandas import DataFrame, Series

from pyds import isEqual, set, shuffle, sort


class ShuffleTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=1000)
        b = shuffle(a)
        self.assertFalse(isEqual(a, b), msg="Failed to shuffle an array!")
        self.assertTrue(isEqual(shape(a), shape(b)), msg="Failed to shuffle an array!")

        self.assertTrue(
            isEqual(sort(set(a)), sort(set(b))), msg="Failed to shuffle an array!"
        )

        a = normal(size=[10, 10, 10, 10])
        b = shuffle(a)

        self.assertFalse(isEqual(a, b), msg="Failed to shuffle an array!")
        self.assertTrue(isEqual(shape(a), shape(b)), msg="Failed to shuffle an array!")

        self.assertTrue(
            isEqual(sort(set(a)), sort(set(b))), msg="Failed to shuffle an array!"
        )

        a = Series(normal(size=1000))
        b = shuffle(a)
        self.assertTrue(isEqual(sort(set(a)), sort(set(b))))

        a = DataFrame(normal(size=[10, 10]))
        b = shuffle(a)
        self.assertTrue(isEqual(sort(set(a)), sort(set(b))))

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
            self.assertRaises(AssertionError, shuffle, item)
