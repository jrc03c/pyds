import unittest
from pyds import containsOnlyNumbers
from numpy.random import *


class ContainsOnlyNumbersTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            containsOnlyNumbers([2, 3, 4]),
            True,
            msg="Fails to detect that an array contains only numbers!",
        )

        self.assertEqual(
            containsOnlyNumbers(normal(size=[5, 5, 5, 5])),
            True,
            msg="Fails to detect that a tensor contains only numbers!",
        )

        self.assertEqual(
            containsOnlyNumbers(["foo", "bar", "baz"]),
            False,
            msg="Fails to detect that an array of strings does not contain only numbers!",
        )

    def testErrors(self):
        x = True

        self.assertRaises(
            AssertionError, containsOnlyNumbers, x,
        )

        x = "foo"

        self.assertRaises(
            AssertionError, containsOnlyNumbers, x,
        )

        x = {"hello": "world"}

        self.assertRaises(
            AssertionError, containsOnlyNumbers, x,
        )

        x = lambda v: v * 2

        self.assertRaises(
            AssertionError, containsOnlyNumbers, x,
        )
