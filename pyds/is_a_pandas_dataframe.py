import pandas as pd


def is_a_pandas_dataframe(x):
    return type(x) is pd.DataFrame
