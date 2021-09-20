import unittest
from pyds import truncatedSVD, rScore, range
from numpy import zeros, dot, shape
from numpy.random import normal


def diagonalize(s, size=None):
    assert isAVector(s), "`s` must be a vector!"

    if size is None:
        size = len(s)

    out = zeros([size, size])

    for i in range(0, len(s)):
        out[i][i] = s[i]

    return out


class TruncatedSVDTestCase(unittest.TestCase):
    def test(self):
        x = normal(size=[100, 100])
        lastRScore = 1

        u, s, v = truncatedSVD(x, shape(x)[1])
        xPrime = dot(dot(u, s), v)

        self.assertAlmostEqual(
            rScore(x, xPrime),
            1,
            msg="Failed to compute the truncated SVD of a matrix!",
        )

        for rank in range(100, 1, -5):
            u, s, v = truncatedSVD(x, rank)
            xPrime = dot(dot(u, s), v)
            r = rScore(x, xPrime)

            self.assertLessEqual(
                r, lastRScore, msg="Failed to compute the truncated SVD of a matrix!"
            )

            lastRScore = r

    def testErrors(self):
        wrongs = [
            [234, 567],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [normal(size=1000), 1000],
            [normal(size=[10, 10, 10]), 10],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, truncatedSVD, pair[0], pair[1])
