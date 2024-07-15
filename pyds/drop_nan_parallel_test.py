import math

from pandas import Series

from .drop_nan_parallel import drop_nan_parallel
from .is_equal import is_equal


def test():
    a = [2, 3, 4, 5, 6]
    b = [math.nan, 8, 9, 10, 11]
    c = [12, 13, math.nan, 15, 16]
    a, b, c = drop_nan_parallel(a, b, c)
    assert is_equal(a, [3, 5, 6])
    assert is_equal(b, [8, 10, 11])
    assert is_equal(c, [13, 15, 16])

    d = [2, 3, 4, 5, 6]
    e = Series([math.nan, 8, 9, 10, 11])
    f = [12, 13, math.nan, 15, 16]
    d, e, f = drop_nan_parallel(d, e, f)
    assert is_equal(d, [3, 5, 6])
    assert is_equal(e, [8, 10, 11])
    assert is_equal(f, [13, 15, 16])
