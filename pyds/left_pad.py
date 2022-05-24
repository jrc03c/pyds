from .flatten import flatten
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from numpy import array, max


def leftPad(x, biggest=None):
    def helper(x, biggest=None):
        if isATensor(x):
            if biggest is None:
                biggest = max(flatten(x))

            if isAPandasSeries(x) or isAPandasDataFrame(x):
                x = x.values.tolist()

            if isANumpyArray(x):
                x = x.tolist()

            return [helper(v, biggest) for v in x]

        else:
            if biggest is None:
                biggest = x

            assert isANumber(x), "`x` must be a whole number!"
            assert int(x) == x, "`x` must be a whole number!"
            assert x >= 0, "`x` must be a whole number!"

            assert isANumber(x), "`biggest` must be a whole number! (%s)" % biggest
            assert int(biggest) == biggest, "`biggest` must be a whole number!"
            assert biggest >= 0, "`biggest` must be a whole number! (%s)" % biggest

            assert x <= biggest, "`x` must be less than or equal to `biggest`!"

            numberOfZeros = len(str(biggest)) - len(str(x))
            return "0" * numberOfZeros + str(x)

    return array(helper(x, biggest))
