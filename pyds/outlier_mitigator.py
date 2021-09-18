from .is_a_vector import *
from .is_a_pandas_series import *
from .is_binary import *
from .sort import *
from numpy import median, abs, array, where, max, min, log, clip


class OutlierMitigator:
    def __init__(
        self, canClip=True, canLog=True, mustClip=False, mustLog=False, maxScore=5
    ):
        self.canClip = canClip
        self.canLog = canLog
        self.mustClip = mustClip
        self.mustLog = mustLog
        self.maxScore = maxScore
        self.median = 0
        self.mad = 0
        self.exceededMaxScore = False

    def fit(self, x):
        assert isAVector(x), "`x` must be a vector!"
        if isAPandasSeries(x):
            x = x.values
        if isBinary(x):
            return self

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

    def transform(self, x):
        assert isAVector(x), "`x` must be a vector!"
        if isAPandasSeries(x):
            x = x.values
        if isBinary(x):
            return x

        if self.mustClip or (self.canClip and self.exceededMaxScore):
            x = clip(
                x,
                self.median - self.maxScore * self.mad,
                self.median + self.maxScore * self.mad,
            )

        if self.mustLog or (self.canLog and self.exceededMaxScore):
            x = log(x - min(x) + 1)

        return x
