import unittest

from numpy import nan
from numpy.random import normal

from pyds import containsOnlyNumbers


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

        self.assertEqual(
            containsOnlyNumbers([nan, nan, nan]),
            False,
            msg="Fails to detect that an array of NaNs does not contain only numbers!",
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
            self.assertRaises(AssertionError, containsOnlyNumbers, item)
