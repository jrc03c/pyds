from .contains_only_numbers import *
from .filter import *
from .flatten import *
from .is_a_number import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_tensor import *
from .is_binary import *
from .sort import *
from numpy import abs, array, clip, inf, log, max, median, min, reshape, shape, where
import warnings


class OutlierMitigator:
    def __init__(
        self,
        isAllowedToClip=True,
        isAllowedToTakeTheLog=True,
        maxScore=5,
        shouldShowWarnings=True,
    ):
        self.isAllowedToClip = isAllowedToClip
        self.isAllowedToTakeTheLog = isAllowedToTakeTheLog
        self.maxScore = maxScore
        self.median = 0
        self.mad = 0
        self.min = 0
        self.exceededMaxScore = False
        self.shouldShowWarnings = shouldShowWarnings

    def fit(self, x):
        # make sure the data is a tensor
        assert isATensor(x), "`x` must be a vector, matrix, or tensor!"

        if isAPandasSeries(x):
            x = x.values

        if isANumpyArray(x):
            x = x.tolist()

        # turn into a vector
        x = flatten(x)

        # drop NaN values
        x = filter(lambda v: isANumber(v), x)

        if len(x) == 0:
            return self

        # if the data is binary, then don't do anything else
        if isBinary(x):
            return self

        # determine whether the max score was exceeded
        self.min = min(x)
        self.median = median(x)
        self.mad = median(abs(x - self.median))

        if self.mad == 0:
            temp = array(sort(x))
            middle = int(len(temp) / 2)
            low = temp[:middle][where(temp[:middle] < self.median)[0]]
            high = temp[middle:][where(temp[middle:] > self.median)[0]]

            if len(low) == 0:
                before = self.median
            else:
                before = max(low)

            if len(high) == 0:
                after = self.median
            else:
                after = min(high)

            self.mad = (after - before) / 2

            if self.mad == 0:
                return self

        score = max(abs(x - self.median) / self.mad)

        if score > self.maxScore:
            self.exceededMaxScore = True

        return self

    def transform(self, *args):
        def betterMin(x):
            lowest = inf

            for value in flatten(x):
                if isANumber(value) and value < lowest:
                    lowest = value

            return lowest

        assert (
            len(args) > 0
        ), "You must pass at least one vector, matrix, or tensor into the `transform` method!"

        reallyOut = []

        for x in args:
            assert isATensor(x), "`x` must be a vector, matrix, or tensor!"

            if isAPandasSeries(x):
                x = x.values

            if isANumpyArray(x):
                x = x.tolist()

            xShape = shape(x)
            x = flatten(x)

            xClean = filter(lambda v: isANumber(v), x)

            if isBinary(xClean):
                reallyOut.append(reshape(x, xShape))
                continue

            if (
                self.shouldShowWarnings
                and betterMin(x) < self.min
                and self.isAllowedToTakeTheLog
            ):
                if len(args) == 1:
                    message = "Note that the data you passed into the `transform` method has a minimum value that is less than the minimum value of the training set, which means that the transformed data will therefore contain some NaN values (since we'll be trying to take the log of negative numbers)! To avoid acquiring NaNs, either (1) transform your data sets so that the data passed into the `train` method has a minimum value less than or equal to the minimum value of the data passed into the `transform` method, or (2) disable log-taking by passing `isAllowedToTakeTheLog=False` to the `OutlierMitigator` constructor. To suppress this warning, pass `shouldShowWarnings=False` to the `OutlierMitigator` constructor."

                else:
                    message = "Note that one of the data sets you passed into the `transform` method has a minimum value that is less than the minimum value of the training set, which means that the transformation of that data will therefore contain some NaN values (since we'll be trying to take the log of negative numbers)! To avoid acquiring NaNs, either (1) transform your data sets so that the data set passed into the `train` method has a minimum value less than or equal to all of the minimum values of the data sets passed into the `transform` method, or (2) disable log-taking by passing `isAllowedToTakeTheLog=False` to the `OutlierMitigator` constructor. To suppress this warning, pass `shouldShowWarnings=False` to the `OutlierMitigator` constructor."

                warnings.warn(message)

            out = []

            for v in x:
                if self.exceededMaxScore and isANumber(v):
                    if self.isAllowedToClip:
                        v = clip(
                            v,
                            self.median - self.maxScore * self.mad,
                            self.median + self.maxScore * self.mad,
                        )

                    if self.isAllowedToTakeTheLog:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            v = log(v - self.min + 1)

                out.append(v)

            reallyOut.append(reshape(out, xShape))

        if len(reallyOut) == 1:
            return reallyOut[0]

        return tuple(reallyOut)
