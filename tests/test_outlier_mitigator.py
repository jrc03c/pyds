import unittest
from math import floor

from numpy import *
from numpy.random import *
from pandas import DataFrame, Series

from pyds import OutlierMitigator, isEqual, makeKey, round, rScore


class OutlierMitigatorTestCase(unittest.TestCase):
    def test(self):
        # doesn't do anything to binary data
        x = round(random(size=1000))
        gator = OutlierMitigator()
        y = gator.fit(x).transform(x)
        self.assertTrue(isEqual(x, y), msg="Failed to mitigate outliers correctly!")

        # doesn't do anything to data without outliers
        x = random(size=1000)
        gator = OutlierMitigator()
        y = gator.fit(x).transform(x)
        self.assertTrue(isEqual(x, y), msg="Failed to mitigate outliers correctly!")

        x = random(size=1000)
        x[-1] = 1e20
        gator = OutlierMitigator()
        y = gator.fit(x).transform(x)
        self.assertFalse(isEqual(x, y), msg="Failed to mitigate outliers correctly!")

        # neither clip nor log
        x = random(size=1000)
        x[-1] = 1e20
        yTrue = x
        gator = OutlierMitigator(isAllowedToClip=False, isAllowedToTakeTheLog=False)
        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

        # both clip and log
        x = random(size=1000)
        x[-1] = 1e20
        med = median(x)
        mad = median(abs(x - med))
        yTrue = clip(x, med - 5 * mad, med + 5 * mad)
        yTrue = log(yTrue - min(yTrue) + 1)
        gator = OutlierMitigator(isAllowedToClip=True, isAllowedToTakeTheLog=True)
        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

        # both clip and log with custom max score
        x = random(size=1000)
        x[-1] = 1e20
        med = median(x)
        mad = median(abs(x - med))
        maxScore = 3
        yTrue = clip(x, med - maxScore * mad, med + maxScore * mad)
        yTrue = log(yTrue - min(yTrue) + 1)

        gator = OutlierMitigator(
            isAllowedToClip=True, isAllowedToTakeTheLog=True, maxScore=maxScore
        )

        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

        try:
            gator = OutlierMitigator()
            x = Series(normal(size=1000))
            gator.fit(x).transform(x)
            failed = False
        except:
            failed = True

        self.assertFalse(failed, msg="Failed to mitigate outliers correctly!")

        # make sure that multiple data sets can be transformed at once
        train1 = array([1, 2, 3, 4, 1000])
        test1 = array([4, 3, 2, 1])
        gator = OutlierMitigator()
        gator.fit(train1)
        train2, test2 = gator.transform(train1, test1)

        self.assertFalse(
            isEqual(train1, train2), msg="Failed to mitigate outliers correctly!"
        )

        self.assertFalse(
            isEqual(test1, test2), msg="Failed to mitigate outliers correctly!"
        )

        # make sure that nothing goes wrong when there's NaNs involved
        x = random(size=1000).tolist()

        for i in range(0, 100):
            funcs = [
                lambda: True,
                lambda: False,
                lambda: None,
                lambda: random(),
                lambda: makeKey(8),
            ]

            index = int(random() * len(x))
            func = funcs[int(random() * len(funcs))]
            x[index] = func()

        x = array(x)

        gator = OutlierMitigator()
        nothingWentWrong = True

        try:
            gator.fit(x).transform(x)
        except:
            nothingWentWrong = False

        self.assertTrue(nothingWentWrong)

        # make sure that tensors are returned in their original shape
        train = [1, 2, 3, 4, 1000]
        gator = OutlierMitigator(shouldShowWarnings=False)
        gator.fit(train)

        test1 = normal(size=[2, 3, 4, 5])
        pred1 = gator.transform(test1)
        self.assertTrue(
            isEqual(shape(test1), shape(pred1)),
            msg="Failed to mitigate outliers correctly!",
        )

        test2 = DataFrame(normal(size=[10, 20]))
        pred2 = gator.transform(test2)
        self.assertTrue(
            isEqual(shape(test2.values), shape(pred2)),
            msg="Failed to migitate outliers correctly!",
        )

    def testErrors(self):
        wrongs = [
            [234, 234],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
        ]

        def helper(a, b):
            gator = OutlierMitigator()
            gator.fit(a).transform(b)

        for pair in wrongs:
            print(pair[0], pair[1])
            self.assertRaises(AssertionError, helper, pair[0], pair[1])
