import unittest

from numpy import array
from numpy.random import normal

from pyds import isEqual, reverse


class ReverseTestCase(unittest.TestCase):
    def test(self):
        x = [1, 3, 5, 6, 4, 2]
        yTrue = array([2, 4, 6, 5, 3, 1])
        yPred = reverse(x)

        self.assertTrue(isEqual(yTrue, yPred), msg="Failed to reverse an array!")

        a = normal(size=[10, 10, 10, 10])
        b = reverse(a)

        for i in range(0, len(a)):
            self.assertTrue(isEqual(a[i], b[-i - 1]), msg="Failed to reverse an array!")

        self.assertEqual(reverse(234), 432, msg="Failed to reverse a number!")
        self.assertEqual(reverse("abc"), "cba", msg="Failed to reverse a string!")

    def testErrors(self):
        wrongs = [
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, reverse, item)
