from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *

# DO NOT import pyds.set!


class Indexer:
    def __init__(self, isVerbose=True):
        assert type(isVerbose) == bool, "`isVerbose` must be a boolean!"
        self.isVerbose = isVerbose

    def fit(self, x):
        assert isAPandasDataFrame(x) or isAPandasSeries(
            x
        ), "`x` must be a pandas DataFrame or Series!"

        self.index = x.dropna().index
        return self

    def mutualFit(self, items):
        for item in items:
            assert isAPandasDataFrame(item) or isAPandasSeries(
                item
            ), "All items must be pandas DataFrames or Series!"

        index = None

        for item in items:
            if index is None:
                index = set(item.dropna().index)
            else:
                index = index.intersection(set(item.dropna().index))

        self.index = list(index)
        return self

    def transform(self, x):
        assert isAPandasDataFrame(x) or isAPandasSeries(
            x
        ), "`x` must be a pandas DataFrame or Series!"

        out = x.loc[self.index]

        if self.isVerbose and out.shape[0] != out.dropna().shape[0]:
            print("WARNING: Indexer transformation has not removed all NaN values!")

        return out
