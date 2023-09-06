import unittest

from numpy import array, inf, isnan, nan
from numpy.random import normal, random
from pandas import DataFrame, Series

from pyds import isEqual, parseFloat

# - numbers
# - strings
# - booleans
# - dictionaries
# - arrays
# - lists
# - vectors
# - matrices
# - tensors
# - numpy `array` and `ndarray`
# - pandas `Series`
# - messy arrays that contain missing and/or non-numerical values
# - pandas `DataFrame`
# - functions
# - objects (instances of classes)
# - None / NaN


class ParseFloatTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(parseFloat(0) == 0)
        self.assertTrue(parseFloat(1) == 1)
        self.assertTrue(parseFloat(-1) == -1)
        self.assertTrue(parseFloat(234.567) == 234.567)
        self.assertTrue(parseFloat(-234.567) == -234.567)
        self.assertTrue(parseFloat("234.567") == 234.567)
        self.assertTrue(parseFloat("-234.567") == -234.567)
        self.assertTrue(parseFloat(inf) == inf)
        self.assertTrue(parseFloat(-inf) == -inf)
        self.assertTrue(parseFloat("inf") == inf)
        self.assertTrue(parseFloat("-inf") == -inf)
        self.assertTrue(isnan(parseFloat("Hello, world!")))
        self.assertTrue(parseFloat(True) == 1)
        self.assertTrue(parseFloat(False) == 0)
        self.assertTrue(isnan(parseFloat({"foo": "bar"})))
        self.assertTrue(isnan(parseFloat(lambda x: x)))
        self.assertTrue(isnan(parseFloat(self)))
        self.assertTrue(isnan(parseFloat(None)))
        self.assertTrue(isnan(parseFloat(nan)))

        a = [2, [3, "4", ["5.67", "hello"]]]
        bTrue = [2, [3, 4, [5.67, nan]]]
        bPred = parseFloat(a)
        self.assertTrue(isEqual(bPred, bTrue))

        c = Series(["foo", "bar", "-234.567", "inf", True, None, "nope"])
        dTrue = Series([nan, nan, -234.567, inf, 1, nan, nan])
        dPred = parseFloat(c)

        print(dTrue)
        print(dPred)

        self.assertTrue(isEqual(dPred, dTrue))

        e = DataFrame([[-1, 0, 1], ["1/3", "234", 567], [True, False, lambda x: x]])
        fTrue = DataFrame([[-1, 0, 1], [nan, 234, 567], [1, 0, nan]])
        fPred = parseFloat(e)
        self.assertTrue(isEqual(fPred, fTrue))

        gTrue = normal(size=1000)

        for i in range(0, 100):
            gTrue[int(random() * len(gTrue))] = nan

        gPred = parseFloat(array([str(v) for v in gTrue.tolist()]))
        self.assertTrue(isEqual(gPred, gTrue))
