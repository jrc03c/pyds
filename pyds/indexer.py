from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series

# DO NOT import pyds.set!


class Indexer:
    def __init__(self, isVerbose=True):
        assert isinstance(isVerbose, bool, "`isVerbose` must be a boolean!")
        self.isVerbose = isVerbose

    def fit(self, *args):
        for item in args:
            assert (
                is_a_pandas_dataframe(item) or is_a_pandas_series(item)
            ), "All items passed into the `fit` method must be pandas DataFrames or Series!"

        index = None

        for item in args:
            if index is None:
                index = set(item.dropna().index)
            else:
                index = index.intersection(set(item.dropna().index))

        self.index = list(index)
        return self

    def transform(self, *args):
        assert (
            len(args) > 0
        ), "You must pass at least one pandas DataFrame or Series into the `transform` method!"

        reallyOut = []

        for item in args:
            assert (
                is_a_pandas_dataframe(item) or is_a_pandas_series(item)
            ), "All items passed into the `transform` method must be pandas DataFrames or Series!"

            out = item.loc[self.index]

            if self.isVerbose and out.shape[0] != out.dropna().shape[0]:
                print("WARNING: Indexer transformation has not removed all NaN values!")

            reallyOut.append(out)

        if len(reallyOut) == 1:
            return reallyOut[0]

        return tuple(reallyOut)
