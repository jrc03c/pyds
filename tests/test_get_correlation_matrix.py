import unittest
from pyds import getCorrelationMatrix, flatten
from numpy import *
from numpy.random import *


class GetCorrelationMatrixTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=[1000, 50])
        b = normal(size=[1000, 50])
        c = getCorrelationMatrix(a, b)

        self.assertEqual(
            c.shape,
            (50, 50),
            msg="The computed correlation matrix has the wrong shape!",
        )

        self.assertGreaterEqual(
            min(flatten(c)),
            -1,
            msg="The computed correlation matrix should not have any values less than -1!",
        )

        self.assertLessEqual(
            max(flatten(c)),
            1,
            msg="The computed correlation matrix should not have any values greater than 1!",
        )

        d = normal(size=1000)
        x = [d]

        for i in range(0, 10):
            x.append(d + 0.0001 * normal(size=1000))

        x = transpose(x)
        c = getCorrelationMatrix(x)

        self.assertGreater(
            min(flatten(c)),
            0.95,
            msg="The correlation matrix computed from a matrix with highly-correlated columns should not contain values less than 0.95!",
        )

        self.assertEqual(
            max(flatten(c)),
            1,
            msg="The correlation matrix computed from a matrix with highly-correlated columns should have a main diagonal of ones!",
        )

    def testErrors(self):
        self.assertRaises(AssertionError, getCorrelationMatrix, [1, 2, 3], [4, 5, 6])

        self.assertRaises(
            AssertionError,
            getCorrelationMatrix,
            normal(size=[3, 3, 3]),
            normal(size=[3, 3, 3]),
        )

        self.assertRaises(AssertionError, getCorrelationMatrix, "foo", "bar")

        self.assertRaises(AssertionError, getCorrelationMatrix, True, False)

        self.assertRaises(
            AssertionError, getCorrelationMatrix, 123, 456,
        )

        self.assertRaises(
            AssertionError, getCorrelationMatrix, {"foo": "bar"}, {"hello": "world"}
        )

        self.assertRaises(
            AssertionError, getCorrelationMatrix, lambda x: x * 2, lambda x: x * 3,
        )
