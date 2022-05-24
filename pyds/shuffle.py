from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
import numpy


def shuffle(x):
    assert isATensor(x), "`x` must be a tensor!"

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        x = x.values

    out = numpy.copy(x)
    numpy.random.shuffle(out)
    return out
