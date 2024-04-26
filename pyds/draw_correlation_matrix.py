import seaborn
from numpy import array, max, min

from .flatten import flatten
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe


def draw_correlation_matrix(c, neg_hue=0, pos_hue=120):
    if isinstance(c, list):
        c = array(c)

    assert is_a_numpy_array(c) or is_a_pandas_dataframe(
        c
    ), "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    assert (
        len(c.shape) == 2
    ), "`c` must be a 2-dimensional list, numpy array, or pandas DataFrame!"

    c_flat = flatten(c)

    assert (
        min(c_flat) >= -1 and max(c_flat) <= 1
    ), "`c` must be a correlation matrix, meaning that it must have values between -1 and 1!"

    seaborn.heatmap(
        c, annot=True, cmap=seaborn.diverging_palette(neg_hue, pos_hue, as_cmap=True)
    )
