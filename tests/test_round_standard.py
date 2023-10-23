import unittest
from math import nan

from numpy.random import normal, random
from pandas import DataFrame, Series

from pyds import apply, isEqual, roundStandard, sign


class RoundStandardTestCase(unittest.TestCase):
    def test(self):
        a = DataFrame([[0.1] * 10] * 10)
        bTrue = DataFrame([[0] * 10] * 10)
        bPred = roundStandard(a)
        self.assertTrue(isEqual(bTrue, bPred))

        c = DataFrame([[0.9] * 10] * 10)
        dTrue = DataFrame([[1] * 10] * 10)
        dPred = roundStandard(c)
        self.assertTrue(isEqual(dTrue, dPred))

        e = normal(size=[10, 10]).tolist()
        fTrue = []

        for i in range(0, len(e)):
            row = e[i]
            temp = []

            for j in range(0, len(row)):
                value = row[j]

                if abs(value) - int(abs(value)) < 0.5:
                    temp.append(int(value))

                else:
                    temp.append(int(value) + sign(value))

            fTrue.append(temp)

        fPred = roundStandard(e)
        print(DataFrame(fTrue), "\n")
        print(DataFrame(fPred))
        self.assertTrue(isEqual(fTrue, fPred))

        self.assertEqual(roundStandard(-0.5), -1)
        self.assertEqual(roundStandard(-1.5), -2)
        self.assertEqual(roundStandard(-3.1), -3)
        self.assertEqual(roundStandard(-3.9), -4)

        g = Series(random(size=100))
        hTrue = Series([int(v) if v - int(v) < 0.5 else int(v) + 1 for v in g.tolist()])
        hPred = roundStandard(g)
        self.assertTrue(isEqual(hTrue, hPred))

        i = normal(size=[2, 3, 4, 5, 6]).tolist()

        jTrue = apply(
            lambda v: int(v) if abs(v) - int(abs(v)) < 0.5 else int(v) + sign(v), i
        ).tolist()

        jPred = roundStandard(i)
        self.assertTrue(isEqual(jTrue, jPred))

        k = ["hello", 234, "world", 567.890]
        lTrue = [nan, 234, nan, 568]
        lPred = roundStandard(k)
        self.assertTrue(isEqual(lTrue, lPred))
