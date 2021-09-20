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
        self.assertRaises(AssertionError, makeKey, -234)
