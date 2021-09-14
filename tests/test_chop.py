import unittest
from pyds import chop, distance, isEqual
from numpy.random import *
from pandas import Series, DataFrame


class ChopTestCase(unittest.TestCase):
    def test(self):
        seed(12345)
        a = Series(random(size=100) + 100)
        seed(12345)
        b = random(size=100) + 100

        seed(23456)
        c = DataFrame(random(size=[100, 100]) + 100)
        seed(23456)
        d = random(size=[100, 100]) + 100

        rights = [
            [0, 0],
            [1, 1],
            [-1, -1],
            [1e-20, 0],
            [-(1e-20), 0],
            [a, b],
            [c, d],
        ]

        for pair in rights:
            self.assertTrue(
                isEqual(chop(pair[0]), pair[1]),
                msg="Failed to chop values! (%s, %s)" % (pair[0], pair[1]),
            )

    def testErrors(self):
        wrongs = [
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            ["hello", "world"],
            lambda x: x * 2,
        ]

        for item in wrongs:
            self.assertRaises(
                AssertionError, chop, item,
            )
