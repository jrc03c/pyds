import unittest
from pyds import getCorrelationMatrix, min, max
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
            min(c),
            -1,
            msg="The computed correlation matrix should not have any values less than -1!",
        )

        self.assertLessEqual(
            max(c),
            1,
            msg="The computed correlation matrix should not have any values greater than 1!",
        )

    def testErrors(self):
        pass
