import unittest

import pandas as pd

from pyds import find_all, isEqual


class FindAllTestCase(unittest.TestCase):
    def test(self):
        x = [2, 3, 4, 5, 6, 7]
        yTrue = [5, 6, 7]
        yPred = find_all(lambda v: v > 4, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find all specified values in a vector.",
        )

        x = [2, [3, 4, [5, 6, 7, [8, 9, 10]]]]
        yTrue = [9, 10]
        yPred = find_all(lambda v: v > 8, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find all specified values in a nested, jagged array.",
        )

        x = pd.DataFrame([[2, 3, 4], [5, 6, 7]])
        yTrue = [2]
        yPred = find_all(lambda v: v < 3, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find all specified values in a pandas DataFrame.",
        )

        yTrue = [7]
        yPred = find_all(x, lambda v: v > 6)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find all specified values by reversing the syntax.",
        )

    def testErrors(self):
        wrongs = [
            [[2, 3, 4], [2, 3, 4]],
            [lambda x: x, lambda x: x],
            [234, 234],
            ["foo", "foo"],
            [True, True],
            [False, False],
            [None, None],
            [{}, {}],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, find_all, pair[0], pair[1])
