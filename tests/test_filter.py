import unittest

from numpy import array

from pyds import filter, isEqual


class FilterTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(
            isEqual(filter([1, 2, 3, 4, 5], lambda x: x > 2), array([3, 4, 5])),
            msg="Could not filter a list!",
        )

        self.assertTrue(
            isEqual(
                filter(
                    [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]], lambda x: len(x) < 4
                ),
                array([[1, 2, 3]]),
            ),
            msg="Could not filter a tensor!",
        )

        # make sure that an array of dtype=object is returned when the values
        # are of mixed types!
        def floatify(x):
            try:
                return float(x)
            except:
                return x

        x = [234, "foo", True, False, None, {}, lambda x: x, []]
        yTrue = array([234, True, False], dtype=object)
        yPred = filter(lambda v: isinstance(v, bool or type(v) == int, x))

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to return an array of dtype=object when returning an array of mixed types from the `filter` function!",
        )

    def testErrors(self):
        wrongs = [
            [234, 567],
            ["foo", "bar"],
            [True, False],
            [[2, 3, 4], [2, 3, 4]],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, filter, pair[0], pair[1])
