import unittest

from numpy import dot
from numpy.random import normal
from pandas import DataFrame

from pyds import leastSquares, rScore


class LeastSquaresTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=[100, 75])
        bTrue = normal(size=[75, 50])
        c = dot(a, bTrue)
        bPred = leastSquares(a, c)

        self.assertGreater(
            rScore(bTrue, bPred), 0.99, msg="Failed to solve least squares!"
        )

        d = DataFrame(normal(size=[100, 75]))
        eTrue = DataFrame(normal(size=[75, 50]))
        f = d.dot(eTrue)
        ePred = DataFrame(leastSquares(d, f))

        self.assertGreater(
            rScore(eTrue, ePred), 0.99, msg="Failed to solve least squares!"
        )

    def testErrors(self):
        missing = normal(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            [234, 567],
            ["foo", "bar"],
            [[["foo"]], [["bar"]]],
            [normal(size=100), normal(size=100)],
            [normal(size=[100, 100, 100]), normal(size=[100, 100, 100])],
            [{"hello": "world"}, {"goodbye": "world"}],
            [True, False],
            [None, None],
            [lambda x: x * 2, lambda x: x * 3],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(
                AssertionError,
                leastSquares,
                pair[0],
                pair[1],
            )
