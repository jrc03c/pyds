import unittest

from numpy import transpose
from numpy.random import normal
from pandas import DataFrame

from pyds import flatten, getCorrelationMatrix


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

        e = DataFrame(normal(size=[100, 100]))
        f = DataFrame(normal(size=[100, 100]))

        try:
            getCorrelationMatrix(e, f)
            failed = False
        except:
            failed = True

        self.assertFalse(failed, msg="Failed to get a correlation matrix!")

    def testErrors(self):
        missing = normal(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            [[2, 3, 4], [5, 6, 7]],
            [[["a", "b", "c"]], [["1", "2", "3"]]],
            [234, 567],
            ["foo", "bar"],
            [normal(size=[10, 10, 10]), normal(size=[10, 10, 10])],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, getCorrelationMatrix, pair[0], pair[1])
