import unittest

from numpy.random import random

from pyds import count, filter, flatten, isEqual, round


class CountTestCase(unittest.TestCase):
    def test(self):
        x = [2, 4, 2, 4, 3, 3, 3, 3, 3]
        yTrue = {2: 2, 3: 5, 4: 2}

        self.assertEqual(
            count(x, 2),
            yTrue[2],
            msg="Could not count the items in an array correctly!",
        )

        self.assertEqual(
            count(x, 3),
            yTrue[3],
            msg="Could not count the items in an array correctly!",
        )

        self.assertEqual(
            count(x, 4),
            yTrue[4],
            msg="Could not count the items in an array correctly!",
        )

        self.assertTrue(
            isEqual(count(x), yTrue),
            msg="Could not count the items in an array correctly!",
        )

        x = round(random(size=[2, 3, 4, 5]))

        yTrue = {
            0: len(filter(lambda v: v == 0, flatten(x))),
            1: len(filter(lambda v: v == 1, flatten(x))),
        }

        self.assertTrue(
            isEqual(count(x), yTrue),
            msg="Could not count the items in an array correctly!",
        )

    def testErrors(self):
        pass
