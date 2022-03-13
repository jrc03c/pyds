import unittest
from pyds import Indexer, range, containsOnlyNumbers, isEqual, distance, flatten
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
        indexer.fit(s, t)
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

        # check that the Indexer can fit and transform using multiple data sets
        a = Series([0, 10, 20, None, 40, 50])
        b = Series([None, 1, 2, 3, 4, 5])
        indexer = Indexer()
        indexer.fit(a, b)
        c, d = indexer.transform(a, b)

        self.assertTrue(
            isEqual(c.index, d.index),
            msg="The indexer did not correctly fit from and/or transform multiple data sets! Specifically, the indexes of the transformed sets do not match. (%s vs. %s)"
            % (c.index.tolist(), d.index.tolist()),
        )

        self.assertTrue(
            distance(c, [10, 20, 40, 50]) == 0,
            msg="The indexer did not correctly fit from and/or transform multiple data sets! Specifically, the values of the first transformed set do not match the expected values. (%s vs. %s)"
            % (flatten(c), flatten([10, 20, 40, 50])),
        )

        self.assertTrue(
            distance(d, [1, 2, 4, 5]) == 0,
            msg="The indexer did not correctly fit from and/or transform multiple data sets! Specifically, the values of the second transformed set do not match the expected values. (%s vs. %s)"
            % (flatten(d), flatten([1, 2, 4, 5])),
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
                AssertionError, indexer.fit, item,
            )
