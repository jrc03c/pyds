import scipy
from numpy import abs, array, mean, nan, shape, sqrt, sum

from .drop_nan import drop_nan
from .flatten import flatten
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_binary import is_binary
from .is_equal import is_equal
from .sign import sign


def mode(x):
    return scipy.stats.mode(x)[0]


class RScoreManager:
    def __init__(self, should_drop_nan_values=False):
        self.num = 0
        self.den = 0
        self.should_drop_nan_values = should_drop_nan_values

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

        assert is_equal(
            shape(true), shape(pred)
        ), "`true` and `pred` must have the same shape!"

        helper = mode if is_binary(baseline) else mean

        true_flattened = flatten(true)
        pred_flattened = flatten(pred)
        baseline_flattened = flatten(baseline)

        if self.should_drop_nan_values:
            true_temp = []
            pred_temp = []

            for i in range(0, len(true_flattened)):
                v_true = true[i]
                v_pred = pred[i]

                if is_a_number(v_true) and is_a_number(v_pred):
                    true_temp.append(v_true)
                    pred_temp.append(v_pred)

            true_flattened = array(true_temp)
            pred_flattened = array(pred_temp)
            baseline_flattened = drop_nan(baseline_flattened)

        self.num += sum((true_flattened - pred_flattened) ** 2)
        self.den += sum((true_flattened - helper(baseline_flattened)) ** 2)
        return self

    def compute(self):
        if self.den == 0:
            return nan

        if not is_a_number(self.num):
            return nan

        if not is_a_number(self.den):
            return nan

        r2 = 1 - self.num / self.den

        if not is_a_number(r2):
            return nan

        return sign(r2) * sqrt(abs(r2))
