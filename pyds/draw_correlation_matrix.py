from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from numpy import array
import seaborn
import matplotlib.pyplot as plot


def drawCorrelationMatrix(c):
    if type(c) == list:
        c = array(c)

    assert isANumpyArray(c) or isAPandasDataFrame(c), "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    assert len(c.shape) == 2, "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    seaborn.heatmap(c, annot=True, cmap=seaborn.diverging_palette(0, 120, as_cmap=True))
    plot.show()
    plot.clf()