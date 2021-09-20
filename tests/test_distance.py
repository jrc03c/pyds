import unittest
from pyds import distance
from numpy.random import normal


class DistanceTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            distance([3, 4], [0, 0]),
            5,
            msg="Cannot get the distance of a vector from zero!",
        )

        self.assertEqual(
            distance([1, 2, 3], [4, 5, 6]),
            27 ** 0.5,
            msg="Cannot get the distance from one vector to another!",
        )

        self.assertEqual(
            distance(3, 5), 2, msg="Cannot get the distance between two numbers!"
        )

    def testErrors(self):
        missing = normal(size=[100, 100])
        missing[0][0] = None

        wrongs = [
            [[2, 3, 4], [2, 3, 4, 5]],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [missing, missing],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, distance, pair[0], pair[1])
