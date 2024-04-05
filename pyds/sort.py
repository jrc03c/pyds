from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


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


def alphasort(a, b):
    if a < b:
        return -1

    if a > b:
        return 1

    return 0


def sort(a, b=None):
    if isATensor(a):
        x = a
        fn = b
    else:
        x = b
        fn = a

    assert isATensor(x), "`x` must be a tensor!"

    if isANumpyArray(x):
        x = x.tolist()

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        x = x.values.tolist()

    if fn is None:
        fn = alphasort

    assert type(fn) == type(sort), "`fn` must be a function!"

    def helper(x, fn):
        if len(x) <= 1:
            return x

        m = int(len(x) / 2)
        a = helper(x[:m], fn)
        b = helper(x[m:], fn)
        return merge(a, b, fn)

    return helper(x, fn)
