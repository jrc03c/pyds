import warnings

from numpy import abs, array, clip, inf, log, max, median, min, reshape, shape, where

from .filter import filter
from .flatten import flatten
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_binary import is_binary
from .sort import sort


class OutlierMitigator:
    def __init__(
        self,
        is_allowed_to_clip=True,
        is_allowed_to_take_the_log=True,
        max_score=5,
        should_show_warnings=True,
    ):
        self.is_allowed_to_clip = is_allowed_to_clip
        self.is_allowed_to_take_the_log = is_allowed_to_take_the_log
        self.max_score = max_score
        self.median = 0
        self.mad = 0
        self.min = 0
        self.exceeded_max_score = False
        self.should_show_warnings = should_show_warnings

    def fit(self, x):
        # make sure the data is a tensor
        assert is_a_tensor(x), "`x` must be a vector, matrix, or tensor!"

        if is_a_pandas_series(x):
            x = x.values

        if is_a_numpy_array(x):
            x = x.tolist()

        # turn into a vector
        x = flatten(x)

        # drop NaN values
        x = filter(lambda v: is_a_number(v), x)

        if len(x) == 0:
            return self

        # if the data is binary, then don't do anything else
        if is_binary(x):
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

        if score > self.max_score:
            self.exceeded_max_score = True

        return self

    def transform(self, *args):
        def better_min(x):
            lowest = inf

            for value in flatten(x):
                if is_a_number(value) and value < lowest:
                    lowest = value

            return lowest

        assert (
            len(args) > 0
        ), "You must pass at least one vector, matrix, or tensor into the `transform` method!"

        really_out = []

        for x in args:
            assert is_a_tensor(x), "`x` must be a vector, matrix, or tensor!"

            if is_a_pandas_series(x):
                x = x.values

            if is_a_numpy_array(x):
                x = x.tolist()

            x_shape = shape(x)
            x = flatten(x)

            x_clean = filter(lambda v: is_a_number(v), x)

            if is_binary(x_clean):
                really_out.append(reshape(x, x_shape))
                continue

            if (
                self.should_show_warnings
                and better_min(x) < self.min
                and self.is_allowed_to_take_the_log
            ):
                if len(args) == 1:
                    message = "Note that the data you passed into the `transform` method has a minimum value that is less than the minimum value of the training set, which means that the transformed data will therefore contain some NaN values (since we'll be trying to take the log of negative numbers)! To avoid acquiring NaNs, either (1) transform your data sets so that the data passed into the `train` method has a minimum value less than or equal to the minimum value of the data passed into the `transform` method, or (2) disable log-taking by passing `is_allowed_to_take_the_log=False` to the `OutlierMitigator` constructor. To suppress this warning, pass `should_show_warnings=False` to the `OutlierMitigator` constructor."

                else:
                    message = "Note that one of the data sets you passed into the `transform` method has a minimum value that is less than the minimum value of the training set, which means that the transformation of that data will therefore contain some NaN values (since we'll be trying to take the log of negative numbers)! To avoid acquiring NaNs, either (1) transform your data sets so that the data set passed into the `train` method has a minimum value less than or equal to all of the minimum values of the data sets passed into the `transform` method, or (2) disable log-taking by passing `is_allowed_to_take_the_log=False` to the `OutlierMitigator` constructor. To suppress this warning, pass `should_show_warnings=False` to the `OutlierMitigator` constructor."

                warnings.warn(message)

            out = []

            for v in x:
                if self.exceeded_max_score and is_a_number(v):
                    if self.is_allowed_to_clip:
                        v = clip(
                            v,
                            self.median - self.max_score * self.mad,
                            self.median + self.max_score * self.mad,
                        )

                    if self.is_allowed_to_take_the_log:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            v = log(v - self.min + 1)

                out.append(v)

            really_out.append(reshape(out, x_shape))

        if len(really_out) == 1:
            return really_out[0]

        return tuple(really_out)
