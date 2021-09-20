import unittest
from pyds import filter, isEqual
from numpy import array


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
