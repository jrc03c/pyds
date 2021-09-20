import unittest
from pyds import rScore
from numpy import shape
from numpy.random import normal
from pandas import Series


class RScoreTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=[10, 10, 10, 10])
        lastRScore = 1

        self.assertEqual(
            rScore(a, a),
            1,
            msg="Failed to compute the correct R-score for two tensors!",
        )

        for scalar in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
            b = a + scalar * normal(size=shape(a))
            r = rScore(a, b)

            self.assertLessEqual(
                r,
                lastRScore,
                msg="Failed to compute the correct R-score for two tensors!",
            )

            lastRScore = r

        c = Series(normal(size=1000))

        self.assertEqual(
            rScore(c, c),
            1,
            msg="Failed to compute the correct R-score for two tensors!",
        )

    def testErrors(self):
        missing = normal(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            [234, 567],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye", "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, rScore, pair[0], pair[1])
