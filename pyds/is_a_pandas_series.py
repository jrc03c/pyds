import pandas as pd


def is_a_pandas_series(x):
    return type(x) is pd.Series
