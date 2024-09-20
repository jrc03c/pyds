import scipy
from numpy import array, mean, nan, shape, sum

from .flatten import flatten
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_binary import is_binary
from .is_equal import is_equal


def mode(x):
    return scipy.stats.mode(x)[0]


def r_squared(true, pred, baseline=None):
    if baseline is None:
        baseline = true

    assert is_a_tensor(true), "`true` must be a vector, matrix, or tensor!"
    assert is_a_tensor(pred), "`pred` must be a vector, matrix, or tensor!"
    assert is_a_tensor(baseline), "`baseline` must be a vector, matrix, or tensor!"

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

    assert is_equal(
        shape(true), shape(pred)
    ), "The vectors, matrices, or tensors passed into the `r_squared` function must all have the same shape!"

    assert is_equal(
        shape(true), shape(baseline)
    ), "The vectors, matrices, or tensors passed into the `r_squared` function must all have the same shape!"

    if is_binary(baseline):
        helper = mode

    else:
        helper = mean

    true = flatten(true)
    pred = flatten(pred)
    baseline = flatten(baseline)

    num = sum((true - pred) ** 2)
    den = sum((true - helper(baseline)) ** 2)

    if den == 0:
        return nan

    return 1 - num / den
