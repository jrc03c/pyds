from scipy.stats import ttest_ind

from .contains_only_numbers import contains_only_numbers
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_series import is_a_pandas_series
from .is_a_vector import is_a_vector


def p_value(a, b):
    assert is_a_vector(a), "`a` must be a vector!"
    assert is_a_vector(b), "`b` must be a vector!"
    assert contains_only_numbers(a), "`a` must contain only numbers!"
    assert contains_only_numbers(b), "`b` must contain only numbers!"

    if is_a_numpy_array(a):
        a = a.tolist()

    if is_a_numpy_array(b):
        b = b.tolist()

    if is_a_pandas_series(a):
        a = a.values

    if is_a_pandas_series(b):
        b = b.values

    return ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
