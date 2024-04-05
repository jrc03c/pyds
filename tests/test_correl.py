import unittest

from numpy.random import normal, random

from pyds import correl


class CorrelTestCase(unittest.TestCase):
    def test(self):
        a = random(size=99999)
        b = random(size=99999)

        self.assertAlmostEqual(
            correl(a, a), 1, msg="The correlation of two identical vectors should be 1!"
        )

        self.assertAlmostEqual(
            correl(a, -a),
            -1,
            msg="The correlation of two equal but opposite vectors should be -1!",
        )

        self.assertLess(
            abs(correl(a, b)),
            0.01,
            msg="The correlation of two random vectors should be close to 0!",
        )

        a = random(size=99999)
        b = a + 1e-5 * normal(size=99999)

        self.assertGreater(
            abs(correl(a, b)),
            0.99,
            msg="The correlation of two almost-identical vectors should be close to 1!",
        )

    def testErrors(self):
        missing = normal(size=1000)
        missing[0] = None

        wrongs = [
            [234, 234],
            [["two", "three", "four"], ["five", "six", "seven"]],
            [normal(size=[50, 50]), normal(size=[50, 50])],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, correl, pair[0], pair[1])
