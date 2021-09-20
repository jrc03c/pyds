import unittest
from pyds import makeKey
from numpy.random import random


class MakeKeyTestCase(unittest.TestCase):
    def test(self):
        for i in range(0, 100):
            n = int(random() * 100)

            self.assertEqual(
                len(makeKey(n)),
                n,
                msg="Failed to generate a key of the correct length!",
            )

    def testErrors(self):
        wrongs = [
            -234,
            123.456,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, makeKey, item)
