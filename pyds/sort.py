from .is_a_tensor import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *


def merge(a, b, fn):
    ai = 0
    bi = 0
    out = []

    while ai < len(a) and bi < len(b):
        if fn(a[ai], b[bi]) < 0:
            out.append(a[ai])
            ai += 1

        else:
            out.append(b[bi])
            bi += 1

    out += a[ai:]
    out += b[bi:]
    return out


def sort(x, fn=None):
    assert isATensor(x), "`x` must be a tensor!"

    if isANumpyArray(x):
        x = x.tolist()

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        x = x.values

    if fn is None:
        fn = lambda a, b: a - b

    assert type(fn) == type(sort), "`fn` must be a function!"

    if len(x) <= 1:
        return x

    m = int(len(x) / 2)
    a = sort(x[:m], fn)
    b = sort(x[m:], fn)
    return merge(a, b, fn)
