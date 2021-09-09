import unittest
from pyds import chop, distance
from numpy.random import *


class ChopTestCase(unittest.TestCase):
    def test(self):
        a = random() + 1
        self.assertEqual(chop(a), a, msg="Cannot chop a positive number!")

        b = -1 - random()
        self.assertEqual(chop(b), b, msg="Cannot chop a negative number!")

        self.assertEqual(chop(0), 0, msg="Cannot chop zero!")

        self.assertEqual(
            chop(1e-20), 0, msg="Cannot chop a very small positive number!"
        )

        self.assertEqual(
            chop(-(1e-20)), 0, msg="Cannot chop a very small negative number!"
        )

        a = random(size=[3, 3, 3, 3]) + 100
        self.assertEqual(distance(chop(a), a), 0, "Cannot chop a tensor of values!")

    def testErrors(self):
        self.assertRaises(AssertionError, chop, "suey")
        self.assertRaises(AssertionError, chop, True)
        self.assertRaises(AssertionError, chop, lambda x: x)
        self.assertRaises(AssertionError, chop, {"foo": "bar"})
