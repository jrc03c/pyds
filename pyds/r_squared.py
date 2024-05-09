import scipy
from numpy import array, mean, nan, sum

from .contains_only_numbers import contains_only_numbers
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_binary import is_binary


def mode(x):
    return scipy.stats.mode(x)[0]


def r_squared(true, pred, baseline=None):
    if baseline is None:
        baseline = true

    assert is_a_tensor(true), "`true` must be a vector, matrix, or tensor!"
    assert is_a_tensor(pred), "`pred` must be a vector, matrix, or tensor!"
    assert is_a_tensor(baseline), "`baseline` must be a vector, matrix, or tensor!"
    assert contains_only_numbers(true), "`true` must contain only numbers!"
    assert contains_only_numbers(pred), "`pred` must contain only numbers!"
    assert contains_only_numbers(baseline), "`baseline` must contain only numbers!"

    if is_a_pandas_series(true) or is_a_pandas_dataframe(true):
        true = true.values

    if is_a_pandas_series(pred) or is_a_pandas_dataframe(pred):
        pred = pred.values

    if is_a_pandas_series(baseline) or is_a_pandas_dataframe(baseline):
        baseline = baseline.values

    if not is_a_numpy_array(true):
        true = array(true)

    if not is_a_numpy_array(pred):
        pred = array(pred)

    if not is_a_numpy_array(baseline):
        baseline = array(baseline)

    if is_binary(baseline):
        helper = mode

    else:
        helper = mean

    num = sum((true - pred) ** 2)
    den = sum((true - helper(baseline)) ** 2)

    if den == 0:
        return nan

    return 1 - num / den
