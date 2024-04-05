import pandas as pd


def isAPandasDataFrame(x):
    return type(x) is pd.DataFrame
