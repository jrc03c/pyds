import unittest
from pyds import Indexer, range, containsOnlyNumbers
from pandas import DataFrame as DF
from pandas import Series
from numpy import *
from numpy.random import *


class IndexerTestCase(unittest.TestCase):
    def test(self):
        s = Series([5, 4, 3, None, 1])
        indexer = Indexer()
        sPrime = indexer.fit(s).transform(s)
        indexTrue = [0, 1, 2, 4]

        for i in range(0, len(sPrime.index)):
            self.assertEqual(
                sPrime.index[i],
                indexTrue[i],
                msg="The indexer did not correctly drop NaN values from a Series!",
            )

        t = Series([None, 20, None, 40, 50])
        indexer.mutualFit([s, t])
        indexTrue = [1, 4]

        for i in range(0, len(indexer.index)):
            self.assertEqual(
                indexer.index[i],
                indexTrue[i],
                msg="The indexer did not correctly drop NaN values from a pair of Series!",
            )

        x = DF(normal(size=[50, 50]))

        for i in range(0, int(0.1 * x.shape[0] * x.shape[1])):
            row = int(random() * x.shape[0])
            col = int(random() * x.shape[1])
            x.values[row][col] = None

        xPrime = indexer.fit(x).transform(x)

        self.assertTrue(
            containsOnlyNumbers(xPrime.values),
            msg="The indexer did not correctly drop NaN values from a DataFrame!",
        )

    def testErrors(self):
        wrongs = [
            234,
            True,
            "foo",
            {"hello": "world"},
            lambda x: x * 2,
            [2, 3, 4],
            [[[2, 3, 4]]],
        ]

        indexer = Indexer()

        for item in wrongs:
            self.assertRaises(AssertionError, indexer.fit, item)

            self.assertRaises(
                AssertionError, indexer.transform, item,
            )

            self.assertRaises(
                AssertionError, indexer.mutualFit, item,
            )
