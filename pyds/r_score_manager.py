import scipy
from numpy import abs, array, mean, nan, shape, sqrt, sum

from .drop_nan import dropNaN
from .flatten import flatten
from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_binary import isBinary
from .is_equal import isEqual
from .sign import sign


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

        assert is_a_tensor(true), "`true` must be a vector, matrix, or tensor!"
        assert is_a_tensor(pred), "`pred` must be a vector, matrix, or tensor!"

        assert is_a_tensor(
            baseline
        ), "`baseline` must be `None` or a vector, matrix, or tensor!"

        if is_a_pandas_series(true) or is_a_pandas_dataframe(true):
            true = true.values

        if not is_a_numpy_array(true):
            true = array(true)

        if is_a_pandas_series(pred) or is_a_pandas_dataframe(pred):
            pred = pred.values

        if not is_a_numpy_array(pred):
            pred = array(pred)

        if is_a_pandas_series(baseline) or is_a_pandas_dataframe(baseline):
            baseline = baseline.values

        if not is_a_numpy_array(baseline):
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
