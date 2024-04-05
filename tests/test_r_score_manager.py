import unittest

import pandas as pd
from numpy import abs, isnan, mean, nan, sqrt, sum
from numpy.random import normal, random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

from pyds import RScoreManager, rScore, sign


class RScoreManagerTestCase(unittest.TestCase):
    def testPerfectScore(self):
        x = normal(size=1000)
        y = x
        manager = RScoreManager()

        for i in range(0, 10):
            xTemp = x[i * 100 : (i + 1) * 100]
            yTemp = y[i * 100 : (i + 1) * 100]
            manager.update(xTemp, yTemp)

        score = manager.compute()
        self.assertEqual(score, 1)

    def testHighScore(self):
        x = normal(size=[1000, 10])
        y = x + 0.01 * normal(size=x.shape)
        x = pd.DataFrame(x)
        y = pd.DataFrame(y)
        manager = RScoreManager()

        for i in range(0, 10):
            xTemp = x.iloc[range(i * 100, (i + 1) * 100), :]
            yTemp = y.iloc[range(i * 100, (i + 1) * 100), :]
            manager.update(xTemp, yTemp)

        score = manager.compute()
        self.assertGreater(score, 0.90)

    def testLowScore(self):
        x = normal(size=[10, 20, 30])
        y = normal(size=[10, 20, 30])
        manager = RScoreManager()

        for i in range(0, 10):
            xTemp = x[i]
            yTemp = y[i]
            manager.update(xTemp, yTemp)

        score = manager.compute()
        self.assertLess(score, 0)

    def testBaseline(self):
        x = [1, 2, 3, 4, 5]
        y = [8, 8, 8, 8, 8]
        b = [8]
        manager = RScoreManager()
        manager.update(x, y, baseline=b)
        score = manager.compute()
        self.assertEqual(score, 0)

    def testConstants(self):
        true = [6, 6, 6, 6, 6]
        pred = [1, 2, 3, 4, 5]
        manager = RScoreManager()
        manager.update(true, pred)
        score = manager.compute()
        self.assertTrue(isnan(score))

    def testDroppingNaNValues(self):
        x = normal(size=1000)
        y = normal(size=1000)

        for i in range(0, 100):
            index = int(random() * len(x))
            x[index] = None

        for i in range(0, 100):
            index = int(random() * len(y))
            y[index] = nan

        manager = RScoreManager(shouldDropNaNValues=True)
        manager.update(x, y)
        score = manager.compute()
        self.assertFalse(isnan(score))

    def testNotDroppingNaNValues(self):
        x = normal(size=1000)
        y = normal(size=1000)

        for i in range(0, 100):
            index = int(random() * len(x))
            x[index] = None

        for i in range(0, 100):
            index = int(random() * len(y))
            y[index] = nan

        manager = RScoreManager(shouldDropNaNValues=False)
        manager.update(x, y)
        score = manager.compute()
        self.assertTrue(isnan(score))

    def testSingleFoldAgainstRScoreFunction(self):
        x = normal(size=1000)
        y = x + 0.01 * normal(size=x.shape)
        r1 = rScore(x, y)
        r2 = RScoreManager().update(x, y).compute()
        self.assertEqual(r1, r2)

    def testCompareWithManuallySumming(self):
        x = normal(size=[1000, 3])
        y = normal(size=1000)

        x = pd.DataFrame(x)
        y = pd.DataFrame(y)

        kf = KFold(n_splits=10, shuffle=True)
        manager = RScoreManager()
        sseTestVsPred = 0
        sseTestVsBaseline = 0

        for trainIndex, testIndex in kf.split(x):
            xTrain = x.iloc[trainIndex, :].values
            xTest = x.iloc[testIndex, :].values
            yTrain = y.iloc[trainIndex].values
            yTest = y.iloc[testIndex].values

            model = LinearRegression()
            model.fit(xTrain, yTrain)
            yPred = model.predict(xTest)

            manager.update(yTest, yPred, baseline=yTrain)
            sseTestVsPred += sum((yTest - yPred) ** 2)
            sseTestVsBaseline += sum((yTest - mean(yTrain)) ** 2)

        score1 = manager.compute()

        r2 = 1 - sseTestVsPred / sseTestVsBaseline
        score2 = sign(r2) * sqrt(abs(r2))

        self.assertLess(abs(score1 - score2), 0.01)

    def testErrors(self):
        wrongs = [
            [[2, 3, 4], 234],
            [[2, 3, 4], "foo"],
            [[2, 3, 4], True],
            [[2, 3, 4], False],
            [[2, 3, 4], None],
            [[2, 3, 4], nan],
            [[2, 3, 4], {}],
            [[2, 3, 4], lambda x: x],
            [234, [2, 3, 4]],
            ["foo", [2, 3, 4]],
            [True, [2, 3, 4]],
            [False, [2, 3, 4]],
            [None, [2, 3, 4]],
            [nan, [2, 3, 4]],
            [{}, [2, 3, 4]],
            [lambda x: x, [2, 3, 4]],
        ]

        for pair in wrongs:
            manager = RScoreManager()
            self.assertRaises(Exception, manager.update, pair[0], pair[1])
