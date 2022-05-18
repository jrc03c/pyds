from .drop_nan import dropNaN
from .flatten import flatten
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_binary import isBinary
from .is_equal import isEqual
from .sign import sign
from numpy import abs, array, mean, nan, shape, sqrt, sum
import scipy


def mode(x):
    return scipy.stats.mode(x)[0]


class RScoreManager:
    def __init__(self, shouldDropNaNValues=False):
        self.num = 0
        self.den = 0
        self.shouldDropNaNValues = shouldDropNaNValues

    def update(self, true, pred, baseline=None):
        if baseline is None:
            baseline = true

        assert isATensor(true), "`true` must be a vector, matrix, or tensor!"
        assert isATensor(pred), "`pred` must be a vector, matrix, or tensor!"

        assert isATensor(
            baseline
        ), "`baseline` must be `None` or a vector, matrix, or tensor!"

        if isAPandasSeries(true) or isAPandasDataFrame(true):
            true = true.values

        if not isANumpyArray(true):
            true = array(true)

        if isAPandasSeries(pred) or isAPandasDataFrame(pred):
            pred = pred.values

        if not isANumpyArray(pred):
            pred = array(pred)

        if isAPandasSeries(baseline) or isAPandasDataFrame(baseline):
            baseline = baseline.values

        if not isANumpyArray(baseline):
            baseline = array(baseline)

        assert isEqual(
            shape(true), shape(pred)
        ), "`true` and `pred` must have the same shape!"

        helper = mode if isBinary(baseline) else mean

        trueFlattened = flatten(true)
        predFlattened = flatten(pred)
        baselineFlattened = flatten(baseline)

        if self.shouldDropNaNValues:
            trueTemp = []
            predTemp = []

            for i in range(0, len(trueFlattened)):
                vTrue = true[i]
                vPred = pred[i]

                if isANumber(vTrue) and isANumber(vPred):
                    trueTemp.append(vTrue)
                    predTemp.append(vPred)

            trueFlattened = array(trueTemp)
            predFlattened = array(predTemp)
            baselineFlattened = dropNaN(baselineFlattened)

        self.num += sum((trueFlattened - predFlattened) ** 2)
        self.den += sum((trueFlattened - helper(baselineFlattened)) ** 2)
        return self

    def compute(self):
        if self.den == 0:
            return nan

        if not isANumber(self.num):
            return nan

        if not isANumber(self.den):
            return nan

        r2 = 1 - self.num / self.den

        if not isANumber(r2):
            return nan

        return sign(r2) * sqrt(abs(r2))
