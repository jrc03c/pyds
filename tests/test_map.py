import unittest
from pyds import map, isEqual
from numpy.random import normal


class MapTestCase(unittest.TestCase):
    def test(self):
        yPred = map(lambda x: x * 2, [2, 3, 4])
        yTrue = [4, 6, 8]

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to apply a function to an array using the `map` function!",
        )

        yPred = map([2, 3, 4], lambda x: x * 2)
        yTrue = [4, 6, 8]

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to apply a function to an array using the `map` function!",
        )

    def testErrors(self):
        identity = lambda x: x

        wrongs = [
            [identity, "foo"],
            ["foo", identity],
            [[2, 3, 4], "foo"],
            ["foo", [2, 3, 4]],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [identity, identity],
            [[2, 3, 4], [2, 3, 4]],
            [234, 234],
        ]

        for pair in wrongs:
            self.assertRaises(
                AssertionError, map, pair[0], pair[1],
            )
