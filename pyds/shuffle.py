from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
import numpy


def shuffle(x):
    assert isATensor(x), "`x` must be a tensor!"

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        x = x.values

    out = numpy.copy(x)
    numpy.random.shuffle(out)
    return out.tolist()
