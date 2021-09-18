import unittest
from pyds import OutlierMitigator, isEqual, rScore
from numpy import *
from numpy.random import *
from pandas import Series, DataFrame

round = vectorize(round)


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

        # clip but don't log
        x = random(size=1000)
        x[-1] = 1e20
        med = median(x)
        mad = median(abs(x - med))
        yTrue = clip(x, med - 5 * mad, med + 5 * mad)
        gator = OutlierMitigator(mustClip=True, canLog=False)
        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

        # log but don't clip
        x = random(size=1000)
        x[-1] = 1e20
        yTrue = log(x - min(x) + 1)
        gator = OutlierMitigator(canClip=False, mustLog=True)
        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

        # neither clip nor log
        x = random(size=1000)
        x[-1] = 1e20
        yTrue = x
        gator = OutlierMitigator(canClip=False, canLog=False)
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
        gator = OutlierMitigator(canClip=True, canLog=True)
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
        gator = OutlierMitigator(canClip=True, canLog=True, maxScore=maxScore)
        yPred = gator.fit(x).transform(x)

        self.assertAlmostEqual(
            rScore(yTrue, yPred), 1, msg="Failed to mitigate outliers correctly!"
        )

    def testErrors(self):
        wrongs = [
            [234, 234],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [normal(size=100), normal(size=[10, 10])],
            [normal(size=[10, 10]), normal(size=100)],
        ]

        def helper(a, b):
            gator = OutlierMitigator()
            gator.fit(a).transform(b)

        for pair in wrongs:
            self.assertRaises(AssertionError, helper, pair[0], pair[1])
