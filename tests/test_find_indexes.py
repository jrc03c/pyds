from pyds import findIndexes, isEqual
import pandas as pd
import unittest


class FindTestCase(unittest.TestCase):
    def test(self):
        x = [2, 3, 4, 5, 6, 7]
        yTrue = [[3], [4], [5]]
        yPred = findIndexes(lambda v: v > 4, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find the indexes of the specified values in a vector.",
        )

        x = [2, [3, 4, [5, 6, 7, [8, 9, 10]]]]
        yTrue = [[1, 2, 3, 1], [1, 2, 3, 2]]
        yPred = findIndexes(lambda v: v > 8, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find the indexes of the specified values in a nested, jagged array.",
        )

        for i in range(0, len(yTrue)):
            iTrue = yTrue[i]
            iPred = yPred[i]

            self.assertTrue(
                isEqual(
                    x[iTrue[0]][iTrue[1]][iTrue[2]][iTrue[3]],
                    x[iPred[0]][iPred[1]][iPred[2]][iPred[3]],
                ),
                msg="Could not correctly find the indexes of the specified values in a nested, jagged array.",
            )

        x = pd.DataFrame([[2, 3, 4], [5, 6, 7]])
        yTrue = [[0, 0]]
        yPred = findIndexes(lambda v: v < 3, x)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find the indexes of the specified values in a pandas DataFrame.",
        )

        self.assertTrue(
            isEqual(x.values[0][0], x.values[yPred[0][0]][yPred[0][1]]),
            msg="Could not correctly find the index of a value in a pandas DataFrame.",
        )

        yTrue = [[1, 2]]
        yPred = findIndexes(x, lambda v: v > 6)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Could not correctly find the indexes of the specified value by reversing the syntax.",
        )

        self.assertTrue(
            isEqual(x.values[1][2], x.values[yPred[0][0]][yPred[0][1]]),
            msg="Could not correctly find the indexes of the specified values by reversing the syntax.",
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
            self.assertRaises(AssertionError, findIndexes, pair[0], pair[1])

