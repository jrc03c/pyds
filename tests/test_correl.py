import unittest
from pyds import correl
from numpy import *
from numpy.random import *


class CorrelTestCase(unittest.TestCase):
    def test(self):
        a = random(size=999999)
        b = random(size=999999)

        self.assertLess(
            abs(correl(a, b)),
            0.01,
            msg="The correlation of two random vectors is NOT close to 0!",
        )

        a = random(size=999999)
        b = a + 1e-5 * normal(size=999999)

        self.assertGreater(
            abs(correl(a, b)),
            0.99,
            msg="The correlation of two almost-identical vectors is NOT close to 1!",
        )

    def testErrors(self):
        message = "Should throw an error when attempting to get the correlation of non-vectors!"

        a = normal(size=[50, 50])
        b = normal(size=[50, 50])
        self.assertRaises(AssertionError, correl, a, b)

        a = "foo"
        b = "bar"
        self.assertRaises(AssertionError, correl, a, b)

        a = True
        b = False
        self.assertRaises(AssertionError, correl, a, b)

        a = lambda x: x * 2
        b = lambda x: x * 3
        self.assertRaises(AssertionError, correl, a, b)

        a = {"foo": "bar"}
        b = {"hello": "world"}
        self.assertRaises(AssertionError, correl, a, b)

        a = 234
        b = -234
        self.assertRaises(AssertionError, correl, a, b)
