from .flatten import flatten
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from numpy import array, max, min
import seaborn


def drawCorrelationMatrix(c, neg_hue=0, pos_hue=120):
    if type(c) == list:
        c = array(c)

    assert isANumpyArray(c) or isAPandasDataFrame(c), "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    assert len(c.shape) == 2, "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    cFlat = flatten(c)

    assert min(cFlat) >= -1 and max(cFlat) <= 1, "`c` must be a correlation matrix, meaning that it must have values between -1 and 1!"

    seaborn.heatmap(
        c,
        annot=True,
        cmap=seaborn.diverging_palette(neg_hue, pos_hue, as_cmap=True)
    )