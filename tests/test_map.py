import unittest
from pyds import map, isEqual
from numpy import array
from numpy.random import normal


class MapTestCase(unittest.TestCase):
    def test(self):
        yPred = map(lambda x: x * 2, [2, 3, 4])
        yTrue = array([4, 6, 8])

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to apply a function to an array using the `map` function!",
        )

        yPred = map([2, 3, 4], lambda x: x * 2)
        yTrue = array([4, 6, 8])

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to apply a function to an array using the `map` function!",
        )

        # make sure that an array of dtype=object is returned when the values
        # are of mixed types!
        def floatify(x):
            try:
                return float(x)
            except:
                return x

        x = ["2.3", "4.5", "six point seven"]
        yTrue = array([2.3, 4.5, "six point seven"], dtype=object)
        yPred = map(floatify, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to return an array of dtype=object when returning an array of mixed types from the `map` function!",
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
